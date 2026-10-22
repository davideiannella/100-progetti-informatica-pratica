#!/usr/bin/env python3
"""Execute every preserved P001–P040 suite in disposable copies, without a shell.

CI exit codes: 0 = complete PASS (or explicitly selected PARTIAL_PASS),
1 = failure/integrity error, 2 = skipped dependency or test. No skip is a PASS.
MongoDB/Neo4j are dedicated, disposable GitHub service containers only.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import importlib.metadata
import io
import json
import os
from pathlib import Path, PurePosixPath
import re
import shutil
import signal
import sqlite3
import subprocess
import sys
import tempfile
import time

HERE = Path(__file__).resolve().parent
SUPPORTED_TESTS = {'.py', '.java', '.c', '.cpp', '.cs'}
FLAGS = ['-Wall', '-Wextra', '-Werror', '-O1', '-g', '-fsanitize=undefined', '-fno-sanitize-recover=all']
PACKAGES = ['pandas', 'fastapi', 'pydantic', 'httpx']


def safe_file(root: Path, relative: str) -> Path:
    rel = PurePosixPath(relative)
    if rel.is_absolute() or '..' in rel.parts or not rel.parts:
        raise ValueError('unsafe relative path')
    path = root.joinpath(*rel.parts)
    if path.is_symlink() or not path.resolve().is_relative_to(root.resolve()):
        raise ValueError('symlink or path escape')
    if not path.is_file():
        raise FileNotFoundError(relative)
    return path


def integrity(root: Path) -> dict:
    manifest = safe_file(root, 'SOURCE_SHA256.json')
    expected = json.loads(manifest.read_text(encoding='utf-8'))
    mismatches = []
    for relative, digest in expected.items():
        actual = hashlib.sha256(safe_file(root, relative).read_bytes()).hexdigest()
        if actual != digest:
            mismatches.append(relative)
    return {'status': 'PASS' if not mismatches else 'FAIL', 'files_checked': len(expected),
            'manifest_sha256': hashlib.sha256(manifest.read_bytes()).hexdigest(),
            'mismatches': mismatches}


def clean_output(value: str, replacements: dict[str, str]) -> str:
    value = re.sub(r'\x1b\[[0-?]*[ -/]*[@-~]', '', value)
    value = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]', '', value)
    # Do not allow subprocess text to become GitHub workflow commands.
    value = re.sub(r'(?m)^::', '[escaped]::', value)
    for old, new in sorted(replacements.items(), key=lambda item: -len(item[0])):
        value = value.replace(old, new)
    value = re.sub(r'(https?://)[^\s/@]+:[^\s/@]+@', r'\1[redacted]@', value)
    value = re.sub(r'(?i)((?:token|password|secret|authorization)\s*[=:]\s*)[^\s,;]+', r'\1[redacted]', value)
    return value


def child_env() -> dict[str, str]:
    names = ['PATH', 'HOME', 'JAVA_HOME', 'DOTNET_ROOT', 'LD_LIBRARY_PATH', 'TMPDIR',
             'LANG', 'LC_ALL', 'SYSTEMROOT']
    env = {key: os.environ[key] for key in names if key in os.environ}
    env.update(PYTHONDONTWRITEBYTECODE='1', PYTHONHASHSEED='0', PYTHONUTF8='1',
               DOTNET_CLI_TELEMETRY_OPTOUT='1', DOTNET_SKIP_FIRST_TIME_EXPERIENCE='1',
               DOTNET_NOLOGO='1', DOTNET_CLI_WORKLOAD_UPDATE_NOTIFY_DISABLE='true')
    return env


def execute(argv: list[str], cwd: Path, replacements: dict[str, str], *, kind='suite',
            timeout=120, stdin=None, suite_file=None, count_basis=None) -> dict:
    started = time.monotonic()
    result = {'command': [clean_output(str(a), replacements) for a in argv], 'kind': kind,
              'suite_file': suite_file, 'exit_code': None, 'test_count': None,
              'count_basis': count_basis, 'stdout': '', 'stderr': ''}
    try:
        proc = subprocess.Popen(argv, cwd=cwd, env=child_env(), stdin=subprocess.PIPE,
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                text=True, encoding='utf-8', errors='replace', start_new_session=True)
        try:
            stdout, stderr = proc.communicate(stdin, timeout=timeout)
            result['exit_code'] = proc.returncode
        except subprocess.TimeoutExpired:
            os.killpg(proc.pid, signal.SIGKILL)
            stdout, stderr = proc.communicate()
            result['exit_code'] = 124
            stderr += '\nTIMEOUT: process group terminated.\n'
        result.update(stdout=clean_output(stdout, replacements), stderr=clean_output(stderr, replacements))
        counts = re.findall(r'\bRan (\d+) tests?\b', stderr)
        if counts:
            result['test_count'] = sum(map(int, counts))
            result['count_basis'] = 'unittest runtime report'
        skipped = sum(int(n) for n in re.findall(r'\bskipped=(\d+)\b', stderr))
        result['skipped_tests'] = skipped
        result['status'] = 'FAIL' if result['exit_code'] else ('SKIP' if skipped else 'PASS')
        if kind == 'suite' and counts and result['test_count'] == 0:
            result.update(status='FAIL', reason='unittest reported zero executed tests')
    except FileNotFoundError:
        result.update(status='SKIP', reason='Required executable unavailable', stderr='Required executable unavailable')
    result['seconds'] = round(time.monotonic() - started, 3)
    return result


def container_id(name: str) -> str | None:
    value = os.environ.get(name, '')
    if not value:
        return None
    if os.environ.get('GITHUB_ACTIONS') != 'true' or not re.fullmatch(r'[a-f0-9]{12,64}', value):
        raise ValueError(f'{name} must identify a disposable GitHub service container')
    return value


def engine_suite(project: int, copied: Path, replacements: dict[str, str]) -> dict:
    variable = 'MONGO_CONTAINER_ID' if project == 31 else 'NEO4J_CONTAINER_ID'
    container = container_id(variable)
    if not container:
        return {'kind': 'engine_suite', 'status': 'SKIP', 'exit_code': None, 'test_count': None,
                'stdout': '', 'stderr': '', 'reason': f'{variable} unavailable: no real engine test executed'}
    if project == 31:
        original = safe_file(copied, 'mongo/telemetry_examples.js').read_text()
        script = '''db = db.getSiblingDB('p031_ci');
db.dropDatabase();
let checks = 0;
function check(value, message) { if (!value) throw new Error(message); checks++; }
check(db.version() === '8.0.14', 'MongoDB version');
'''
        script += original + '''
check(db.telemetry.countDocuments({}) === 1, 'original insert');
const first = db.telemetry.findOne({deviceId:'sensor-01'});
check(first.ts instanceof Date, 'BSON Date');
check(first.metrics.temperature === 22.4 && first.metrics.humidity === 51, 'original metrics');
const indexes = db.telemetry.getIndexes();
check(indexes.some(i => JSON.stringify(i.key) === JSON.stringify({deviceId:1, ts:-1})), 'compound index and key order');
for (let i=0; i<12; i++) db.telemetry.insertOne({deviceId:'sensor-01',ts:new Date(first.ts.getTime()-(12-i)*1000),metrics:{temperature:i,humidity:50}});
db.telemetry.insertOne({deviceId:'other-device',ts:new Date(first.ts.getTime()+1000),metrics:{temperature:0,humidity:0}});
const actual = db.telemetry.find({deviceId:'sensor-01'}).sort({ts:-1}).limit(10).toArray();
check(actual.length === 10, 'limit 10');
check(actual.every(x => x.deviceId === 'sensor-01'), 'device filter');
check(actual.every(x => x.ts instanceof Date), 'all results use BSON Date');
check(actual.every((x,i) => i === 0 || actual[i-1].ts.getTime() > x.ts.getTime()), 'strict descending order');
check(db.telemetry.countDocuments({deviceId:'sensor-01'}) === 13, 'all source records retained');
check(actual[0]._id.equals(first._id), 'newest original record first');
check(actual[9].metrics.temperature === 3, 'limit selects correct oldest retained record');
print('CI_ENGINE_RESULT=' + JSON.stringify({status:'PASS',checks:checks,version:db.version()}));
'''
        result = execute(['docker', 'exec', '-i', container, 'mongosh', '--quiet', '--file', '/dev/stdin'],
                         copied, replacements, kind='engine_suite', timeout=180, stdin=script)
        lines = [line.removeprefix('CI_ENGINE_RESULT=') for line in result['stdout'].splitlines()
                 if line.startswith('CI_ENGINE_RESULT=')]
        if result['status'] == 'PASS':
            if len(lines) != 1:
                result.update(status='FAIL', reason='MongoDB assertion summary missing')
            else:
                details = json.loads(lines[0])
                result.update(test_count=details['checks'], count_basis='executed MongoDB assertions', engine_version=details['version'])
                if details['checks'] != 12 or details['status'] != 'PASS':
                    result.update(status='FAIL', reason='MongoDB assertion summary incomplete')
        return result
    original = safe_file(copied, 'cypher/mobility.cypher').read_text()
    checks = [
        "CALL dbms.components() YIELD versions RETURN 'CI_ASSERT_version' AS check, versions[0]='5.26.0' AS passed;",
        "MATCH (n:Stop) RETURN 'CI_ASSERT_nodes' AS check, count(n)=3 AS passed;",
        "MATCH ()-[r:CONNECTS]->() RETURN 'CI_ASSERT_edges' AS check, count(r)=3 AS passed;",
        "MATCH (a:Stop)-[r:CONNECTS]->(b:Stop) WITH a,b,r ORDER BY a.id,b.id WITH collect(a.id+'>'+b.id+':'+toString(r.minutes)) AS edges RETURN 'CI_ASSERT_edge_values' AS check, edges=['A>B:5','A>C:20','B>C:7'] AS passed;",
        "MATCH p=(:Stop {id:'A'})-[:CONNECTS*1..4]->(:Stop {id:'C'}) WITH p,reduce(total=0,r IN relationships(p)|total+r.minutes) AS minutes ORDER BY minutes LIMIT 1 RETURN 'CI_ASSERT_shortest' AS check, minutes=12 AND [n IN nodes(p)|n.id]=['A','B','C'] AS passed;",
        "MATCH p=(:Stop {id:'C'})-[:CONNECTS*1..4]->(:Stop {id:'A'}) RETURN 'CI_ASSERT_direction' AS check, count(p)=0 AS passed;",
    ]
    script = 'MATCH (n) DETACH DELETE n;\n' + original + '\n' + original + '\n' + '\n'.join(checks)
    result = execute(['docker', 'exec', '-i', container, 'cypher-shell', '--format', 'plain'],
                     copied, replacements, kind='engine_suite', timeout=180, stdin=script)
    observed = {}
    for row in csv.reader(io.StringIO(result['stdout']), skipinitialspace=True):
        if len(row) == 2 and row[0].startswith('CI_ASSERT_'):
            observed[row[0]] = row[1].strip().lower() == 'true'
    expected = set(re.findall(r"'(CI_ASSERT_\w+)'", '\n'.join(checks)))
    result.update(assertions=observed, test_count=len(observed), count_basis='executed Neo4j assertion queries')
    if result['status'] == 'PASS' and (set(observed) != expected or not all(observed.values())):
        result.update(status='FAIL', reason='Neo4j assertion missing or false')
    return result


def run_project(entry: dict, root: Path, workspace: Path, replacements: dict[str, str]) -> dict:
    pid = entry['project']
    original = root / 'projects' / pid
    if original.is_symlink() or not original.resolve().is_relative_to(root):
        raise ValueError('unsafe project path')
    inventory = sorted(str(p.relative_to(original)) for p in (original / 'tests').rglob('*')
                       if p.is_file() and p.suffix in SUPPORTED_TESTS)
    if inventory != sorted(entry['test_files']):
        raise ValueError(f'{pid}: test inventory differs from reviewed matrix')
    for p in original.rglob('*'):
        if p.is_symlink():
            raise ValueError(f'{pid}: symbolic link rejected')
    copied = workspace / pid
    shutil.copytree(original, copied, ignore=shutil.ignore_patterns('__pycache__', 'bin', 'obj', 'build', '*.log'))
    (copied / 'build').mkdir(exist_ok=True)
    (copied / 'NuGet.ci.config').write_text('<configuration><packageSources><clear /></packageSources></configuration>')
    replacements[str(copied)] = f'<WORK>/{pid}'
    steps = []
    blocked = False
    for step in entry['steps']:
        if blocked:
            steps.append({'kind': step['kind'], 'suite_file': step.get('suite_file'), 'status': 'NOT_RUN',
                          'exit_code': None, 'stdout': '', 'stderr': '', 'reason': 'required build or restore failed'})
            continue
        argv = [sys.executable if arg == '{python}' else arg for arg in step['argv']]
        for relative in step.get('input_files', []):
            safe_file(copied, relative)
        result = execute(argv, copied, replacements, kind=step['kind'], timeout=step.get('timeout', 180),
                         suite_file=step.get('suite_file'),
                         count_basis='standalone assertion program; exit status is the oracle' if step['kind'] == 'suite' else None)
        steps.append(result)
        if step['kind'] in {'build', 'restore'} and result['status'] != 'PASS':
            blocked = True
    if entry.get('engine'):
        steps.append(engine_suite(int(pid[1:]), copied, replacements))
    statuses = {step['status'] for step in steps}
    status = 'FAIL' if 'FAIL' in statuses else ('SKIP' if statuses != {'PASS'} else 'PASS')
    suites = [step for step in steps if step['kind'] in {'suite', 'engine_suite'}]
    return {'project': pid, 'status': status, 'scope': entry['scope'], 'environment': entry['environment'],
            'suite_count_expected': sum(s['kind'] == 'suite' for s in entry['steps']) + bool(entry.get('engine')),
            'suite_count_executed': sum(s.get('exit_code') is not None for s in suites),
            'suite_count_passed': sum(s['status'] == 'PASS' for s in suites),
            'known_test_count': sum(s.get('test_count') or 0 for s in suites),
            'count_note': 'Known count includes unittest runtime reports and engine assertions only; standalone assertion suites are not relabeled as individual test methods.',
            'steps': steps}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=HERE.parents[1])
    parser.add_argument('--output', type=Path, default=Path('artifacts/p001-p040'))
    parser.add_argument('--projects', help='Optional comma-separated P001..P040 selection; reports partial coverage')
    parser.add_argument('--validate-only', action='store_true')
    args = parser.parse_args()
    root = args.root.resolve()
    output = args.output.resolve()
    if output == root or output.is_relative_to(root / 'projects'):
        raise ValueError('Output cannot replace the root or be inside preserved projects')
    output.mkdir(parents=True, exist_ok=True)
    report = {'schema': 1, 'status': 'FAIL', 'requested_range': 'P001–P040', 'projects': []}
    code = 1
    try:
        if sys.flags.optimize:
            raise ValueError('Python optimization disables assertions and is forbidden')
        matrix = json.loads((HERE / 'matriceci.json').read_text())
        if [x['project'] for x in matrix] != [f'P{i:03}' for i in range(1, 41)]:
            raise ValueError('matrix must cover exactly P001..P040')
        selected = set(args.projects.split(',')) if args.projects else {e['project'] for e in matrix}
        if not selected or not selected <= {e['project'] for e in matrix}:
            raise ValueError('invalid project selection')
        report['partial_selection'] = len(selected) != 40
        report['integrity_before'] = integrity(root)
        if report['integrity_before']['status'] != 'PASS':
            raise ValueError('Original source checksum mismatch before execution')
        report['runtime'] = {'python': sys.version, 'platform': sys.platform,
                             'sqlite': sqlite3.sqlite_version, 'packages': {}}
        for package in PACKAGES:
            try:
                report['runtime']['packages'][package] = importlib.metadata.version(package)
            except importlib.metadata.PackageNotFoundError:
                report['runtime']['packages'][package] = None
        if args.validate_only:
            for entry in matrix:
                project_root = root / 'projects' / entry['project']
                actual = sorted(str(p.relative_to(project_root)) for p in (project_root / 'tests').rglob('*')
                                if p.is_file() and p.suffix in SUPPORTED_TESTS)
                if actual != sorted(entry['test_files']):
                    raise ValueError(f"test coverage mismatch: {entry['project']}")
                for step in entry['steps']:
                    for relative in step.get('input_files', []):
                        safe_file(project_root, relative)
            report.update(status='VALIDATED_ONLY', matrix_projects=len(matrix), tests_executed=0)
            code = 0
        else:
            replacements = {str(root): '<SOURCE_ROOT>', str(output): '<ARTIFACTS>'}
            with tempfile.TemporaryDirectory(prefix='p001-p040-') as directory:
                workspace = Path(directory)
                replacements[str(workspace)] = '<WORK>'
                report['toolchain'] = [execute(cmd, workspace, replacements, kind='environment', timeout=30)
                                       for cmd in [['java', '-version'], ['gcc', '--version'], ['g++', '--version'], ['dotnet', '--info']]]
                for entry in matrix:
                    if entry['project'] not in selected:
                        continue
                    result = run_project(entry, root, workspace, replacements)
                    report['projects'].append(result)
                    (output / f"{entry['project']}.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
                    print(f"{entry['project']}: {result['status']}", file=sys.stderr, flush=True)
            statuses = {p['status'] for p in report['projects']}
            report['status'] = 'FAIL' if 'FAIL' in statuses else ('SKIP' if statuses != {'PASS'} else ('PARTIAL_PASS' if report['partial_selection'] else 'PASS'))
            code = 1 if report['status'] == 'FAIL' else (2 if report['status'] == 'SKIP' else 0)
        report['integrity_after'] = integrity(root)
        if report['integrity_before'] != report['integrity_after']:
            report.update(status='FAIL', reason='Original sources or checksum manifest changed')
            code = 1
    except Exception as error:
        report.update(status='FAIL', error=f'{type(error).__name__}: {error}')
        code = 1
    report['exit_code'] = code
    report['project_count_executed'] = len(report['projects'])
    report['project_count_passed'] = sum(p['status'] == 'PASS' for p in report['projects'])
    report['project_count_skipped'] = sum(p['status'] == 'SKIP' for p in report['projects'])
    (output / 'results.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(report, ensure_ascii=False))
    return code


if __name__ == '__main__':
    raise SystemExit(main())
