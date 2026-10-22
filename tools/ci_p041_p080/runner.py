#!/usr/bin/env python3
"""Public CI for frozen P041-P080. Tests run in copies; original bytes never change.

Usage: python runner.py --sources . --out ci-results --projects 41-80
Missing tools, skipped tests and disabled runtime checks never become PASS.
Python unittest method counts and assertion-script suite counts are kept separate.
"""
from __future__ import annotations

import argparse
from contextlib import contextmanager
from datetime import datetime, timezone
import hashlib
import importlib.metadata
import json
import os
from pathlib import Path
import platform
import re
import shutil
import socket
import subprocess
import sys
import time
import traceback
import urllib.error
import urllib.request
import uuid

HERE = Path(__file__).resolve().parent


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def tree_hashes(root):
    return {p.relative_to(root).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in sorted(root.rglob("*")) if p.is_file()}


def unittest_counts(stdout, stderr):
    for line in reversed(stdout.splitlines()):
        candidate = line.removeprefix("TEST_SUMMARY ")
        try:
            report = json.loads(candidate)
        except (ValueError, TypeError):
            continue
        if isinstance(report, dict) and "tests_run" in report:
            return {k: report.get(k, 0) for k in
                    ("tests_run", "failures", "errors", "skipped", "subcases")}
    found = re.search(r"Ran (\d+) tests? in", stderr)
    if found:
        result = {"tests_run": int(found[1]), "failures": 0, "errors": 0, "skipped": 0,
                  "subcases": None}
        for field in ("failures", "errors", "skipped"):
            match = re.search(rf"\b{field}=(\d+)", stderr)
            if match:
                result[field] = int(match[1])
        return result
    return None


class Evidence:
    def __init__(self, project, work, out):
        self.project, self.work, self.out = project, work, out
        self.records = []
        out.mkdir(parents=True, exist_ok=True)
        self.env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", PYTHONHASHSEED="0",
                        OMP_NUM_THREADS="1", OPENBLAS_NUM_THREADS="1", MKL_NUM_THREADS="1",
                        DOTNET_CLI_TELEMETRY_OPTOUT="1", DOTNET_NOLOGO="1")
        self.env.pop("PYTHONOPTIMIZE", None)

    def record(self, item):
        item["sequence"] = len(self.records) + 1
        self.records.append(item)
        write_json(self.out / "steps.json", self.records)
        print(f"{self.project} {item['sequence']:03}: {item.get('name', item.get('command'))} "
              f"{item['status']}", flush=True)
        return item

    def run(self, command, *, name=None, kind="command", timeout=300, strict=True):
        command = [str(x) for x in command]
        start = time.monotonic()
        try:
            result = subprocess.run(command, cwd=self.work, env=self.env, text=True,
                                    capture_output=True, timeout=timeout, encoding="utf-8", errors="replace")
            code, stdout, stderr = result.returncode, result.stdout, result.stderr
            status = "PASS" if code == 0 else "FAIL"
        except FileNotFoundError as exc:
            code, stdout, stderr, status = None, "", str(exc), "BLOCKED"
        except subprocess.TimeoutExpired as exc:
            code, status = None, "TIMEOUT"
            stdout = exc.stdout or ""
            stderr = exc.stderr or ""
            if isinstance(stdout, bytes): stdout = stdout.decode("utf-8", "replace")
            if isinstance(stderr, bytes): stderr = stderr.decode("utf-8", "replace")
        counts = unittest_counts(stdout, stderr) if kind == "test_suite" else None
        if counts and counts["skipped"] and status == "PASS":
            status = "INCOMPLETE"
        seq = len(self.records) + 1
        stem = f"{seq:03}_{re.sub('[^A-Za-z0-9_-]', '_', name or kind)}"
        (self.out / f"{stem}.stdout.log").write_text(stdout, encoding="utf-8")
        (self.out / f"{stem}.stderr.log").write_text(stderr, encoding="utf-8")
        item = self.record({"kind": kind, "name": name or command[0], "command": command,
                            "cwd": str(self.work), "exit_code": code, "status": status,
                            "stdout": stdout, "stderr": stderr,
                            "seconds": round(time.monotonic()-start, 3), "unittest": counts})
        if strict and status != "PASS":
            raise RuntimeError(f"{item['name']}: {status}; see saved stdout/stderr")
        return item

    def check(self, name, condition, detail):
        self.record({"kind": "runtime_check", "name": name,
                     "status": "PASS" if condition else "FAIL", "detail": detail})
        if not condition:
            raise AssertionError(f"{name}: {detail}")

    def skip(self, name, reason):
        self.record({"kind": "runtime_check", "name": name, "status": "SKIPPED", "reason": reason})

    def command_json(self, command, **kwargs):
        return json.loads(self.run(command, **kwargs)["stdout"])


def http_json(base, path, payload=None):
    data = None if payload is None else json.dumps(payload).encode()
    request = urllib.request.Request(base + path, data=data,
                                     headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(request, timeout=5) as response:
            return response.status, json.loads(response.read())
    except urllib.error.HTTPError as exc:
        return exc.code, json.loads(exc.read())


def wait_for(getter, predicate, timeout=120, interval=2):
    deadline = time.monotonic() + timeout
    last = None
    while time.monotonic() < deadline:
        try:
            last = getter()
            if predicate(last):
                return last
        except (OSError, ValueError, RuntimeError) as exc:
            last = repr(exc)
        time.sleep(interval)
    raise TimeoutError(f"Condition not reached in {timeout}s; last={last}")


@contextmanager
def background(ev, command, name):
    stdout_path, stderr_path = ev.out / f"{name}.stdout.log", ev.out / f"{name}.stderr.log"
    with stdout_path.open("w") as stdout, stderr_path.open("w") as stderr:
        proc = subprocess.Popen(command, cwd=ev.work, env=ev.env, stdout=stdout, stderr=stderr)
        try:
            yield proc
        finally:
            proc.terminate()
            try:
                proc.wait(timeout=10)
            except subprocess.TimeoutExpired:
                proc.kill(); proc.wait(timeout=10)
            ev.record({"kind": "background_process", "name": name, "command": command,
                       "status": "STOPPED", "exit_code": proc.returncode,
                       "stdout": stdout_path.read_text(), "stderr": stderr_path.read_text(),
                       "note": "Termination was requested by the runner after the runtime checks."})


def free_port():
    with socket.socket() as sock:
        sock.bind(("127.0.0.1", 0))
        return sock.getsockname()[1]


def docker_api(ev):
    name = "ci-p054-" + uuid.uuid4().hex[:10]
    image = name + ":1"
    ev.run(["docker", "info"], name="docker_info")
    ev.run(["docker", "build", "-t", image, "."], name="docker_build", timeout=600)
    try:
        ev.run(["docker", "run", "-d", "--name", name, "-p", "127.0.0.1::8000", image], name="container_start")
        info = ev.command_json(["docker", "inspect", name], name="container_inspect")[0]
        port = info["NetworkSettings"]["Ports"]["8000/tcp"][0]["HostPort"]
        base = f"http://127.0.0.1:{port}"
        health = wait_for(lambda: http_json(base, "/health"), lambda x: x == (200, {"status": "ok"}))
        ev.check("P054 Docker health HTTP", health == (200, {"status": "ok"}), health)
        created = http_json(base, "/items/1", {"name": "router", "quantity": 2})
        ev.check("P054 Docker POST", created == (200, {"id": 1, "name": "router", "quantity": 2}), created)
        fetched = http_json(base, "/items/1")
        ev.check("P054 Docker GET", fetched == created, fetched)
        invalid = http_json(base, "/items/2", {"name": "router", "quantity": -1})
        ev.check("P054 Docker invalid input", invalid[0] == 422, invalid)
        ev.check("P054 Docker non-root", info["Config"]["User"] == "appuser", info["Config"]["User"])
    finally:
        ev.run(["docker", "logs", name], name="container_logs", kind="diagnostic", strict=False)
        ev.run(["docker", "rm", "-f", name], name="container_cleanup", kind="cleanup", strict=False)


def compose_stack(ev):
    name = "ci-p055-" + uuid.uuid4().hex[:10]
    compose = ["docker", "compose", "-f", "compose.yaml", "-p", name]
    ev.run(["docker", "info"], name="docker_info")
    ev.run(["docker", "compose", "version"], name="compose_version")
    ev.run(compose + ["config", "--quiet"], name="compose_config")
    try:
        ev.run(compose + ["up", "-d", "--build", "--wait", "--wait-timeout", "180"], name="compose_up", timeout=600)
        base = "http://127.0.0.1:8080"
        wait_for(lambda: http_json(base, "/health"), lambda x: x == (200, {"status": "ok"}))
        label = "public-ci-" + uuid.uuid4().hex
        created = http_json(base, "/items", {"name": label})
        ev.check("P055 create through Nginx/API/PostgreSQL", created[0] == 201 and created[1]["name"] == label, created)
        duplicate = http_json(base, "/items", {"name": label})
        ev.check("P055 duplicate HTTP 409", duplicate[0] == 409, duplicate)
        invalid = http_json(base, "/items", {"name": " "})
        ev.check("P055 invalid input HTTP 422", invalid[0] == 422, invalid)
        for service in ("api", "db"):
            ev.run(compose + ["restart", service], name=f"restart_{service}")
            response = wait_for(lambda: http_json(base, "/items"),
                                lambda x: x[0] == 200 and created[1] in x[1], timeout=120)
            ev.check(f"P055 persistence after {service} restart", created[1] in response[1], response)
        version = ev.run(compose + ["exec", "-T", "db", "psql", "-U", "app", "-d", "appdb", "-Atc", "SHOW server_version;"], name="postgresql_version")["stdout"].strip()
        ev.check("P055 native PostgreSQL major version", version.startswith("17."), version)
    finally:
        ev.run(compose + ["ps", "--format", "json"], name="compose_status", kind="diagnostic", strict=False)
        ev.run(compose + ["logs", "--no-color"], name="compose_logs", kind="diagnostic", strict=False)
        ev.run(compose + ["down", "--volumes", "--remove-orphans"], name="compose_cleanup", kind="cleanup", strict=False)


def kubernetes_cluster(ev):
    name = "ci-p056-" + uuid.uuid4().hex[:10]
    context = "kind-" + name
    kube = ["kubectl", "--context", context]
    image = "p056-demo-api:1.0"  # Exactly the frozen deployment's imagePullPolicy: Never image.
    ev.run(["docker", "info"], name="docker_info")
    ev.run(["kind", "version"], name="kind_version")
    ev.run(["kubectl", "version", "--client", "-o", "json"], name="kubectl_version")
    ev.run(["docker", "build", "-t", image, "."], name="docker_build", timeout=600)
    try:
        node_image = "kindest/node:v1.37.0@sha256:a1ed56cfb0e7b93589bdf97c8cd566405a265939e3620fc4f5de89adff580ae5"
        ev.run(["kind", "create", "cluster", "--name", name, "--image", node_image, "--wait", "180s"], name="kind_create", timeout=600)
        ev.run(["kind", "load", "docker-image", image, "--name", name], name="kind_load", timeout=180)
        ev.run(kube + ["apply", "-f", "k8s/deployment.yaml"], name="apply_deployment")
        ev.run(kube + ["rollout", "status", "deployment/demo-api", "--timeout=180s"], name="deployment_ready")
        ev.run(kube + ["-n", "kube-system", "rollout", "status", "deployment/coredns", "--timeout=180s"], name="dns_ready")
        ev.run(kube + ["version", "-o", "json"], name="cluster_versions")

        def pods():
            return ev.command_json(kube + ["get", "pods", "-l", "app=demo-api", "-o", "json"], name="pods")["items"]

        def ready(items):
            return len(items) == 3 and all(not p["metadata"].get("deletionTimestamp") and
                any(c["type"] == "Ready" and c["status"] == "True" for c in p.get("status", {}).get("conditions", []))
                for p in items)

        initial = wait_for(pods, ready)
        ev.check("P056 three ready replicas", ready(initial), [p["metadata"]["name"] for p in initial])
        slices = ev.command_json(kube + ["get", "endpointslices", "-l", "kubernetes.io/service-name=demo-api", "-o", "json"], name="endpointslices")
        endpoints = [e for s in slices["items"] for e in s.get("endpoints", []) if e.get("conditions", {}).get("ready")]
        ev.check("P056 Service has three ready endpoints", len(endpoints) == 3, endpoints)
        for pod in initial:
            result = ev.run(kube + ["exec", pod["metadata"]["name"], "--", "python", "-c",
                "import urllib.request; print(urllib.request.urlopen('http://demo-api/health',timeout=5).read().decode())"], name="in_cluster_service")
            ev.check("P056 in-cluster Service HTTP", json.loads(result["stdout"]) == {"status": "ok"}, result["stdout"])
        port = free_port()
        with background(ev, kube + ["port-forward", "service/demo-api", f"{port}:80"], "service_forward"):
            response = wait_for(lambda: http_json(f"http://127.0.0.1:{port}", "/health"), lambda x: x == (200, {"status": "ok"}), timeout=30)
            ev.check("P056 Service HTTP via port-forward", response[0] == 200, response)
        removed = initial[0]
        ev.run(kube + ["delete", "pod", removed["metadata"]["name"], "--wait=true", "--timeout=90s"], name="delete_one_pod", timeout=120)
        replacement = wait_for(pods, lambda x: ready(x) and removed["metadata"]["uid"] not in {p["metadata"]["uid"] for p in x})
        ev.check("P056 deleted Pod recreated", ready(replacement), [p["metadata"]["uid"] for p in replacement])

        victim = replacement[0]
        pod_name = victim["metadata"]["name"]
        status = victim["status"]["containerStatuses"][0]
        container_id = status["containerID"].split("://", 1)[1]
        restart_before = status["restartCount"]
        node = victim["spec"]["nodeName"]
        # Stop the actual Linux container task, as in the successful historical runtime test.
        ev.run(["docker", "exec", node, "ctr", "--namespace", "k8s.io", "tasks", "kill", "--signal", "SIGSTOP", container_id], name="liveness_fault_SIGSTOP")
        def victim_state():
            return ev.command_json(kube + ["get", "pod", pod_name, "-o", "json"], name="liveness_poll")
        recovered = wait_for(victim_state, lambda p: any(s["restartCount"] > restart_before and s["ready"]
                             for s in p.get("status", {}).get("containerStatuses", [])), timeout=240, interval=3)
        ev.check("P056 liveness restart and ready", recovered["status"]["containerStatuses"][0]["restartCount"] > restart_before, recovered["status"]["containerStatuses"])
        events = ev.command_json(kube + ["get", "events", "--field-selector", f"involvedObject.name={pod_name}", "-o", "json"], name="liveness_events")
        messages = [e.get("message", "") for e in events["items"]]
        ev.check("P056 liveness failure observed", any("Liveness probe failed" in m for m in messages), messages)
        final = wait_for(pods, ready)
        ev.check("P056 all replicas recovered", ready(final), [p["metadata"]["name"] for p in final])
    finally:
        ev.run(kube + ["get", "pods", "-o", "wide"], name="final_pods", kind="diagnostic", strict=False)
        ev.run(kube + ["get", "events", "-o", "json"], name="final_events", kind="diagnostic", strict=False)
        ev.run(["kind", "delete", "cluster", "--name", name], name="kind_cleanup", kind="cleanup", timeout=180, strict=False)


def execute_project(entry, sources, out, skip_runtime):
    project = entry["project"]
    original = sources / "projects" / project
    before = tree_hashes(original)
    work = out / "work" / project
    if work.exists():
        raise FileExistsError(f"Output work directory already exists: {work}")
    shutil.copytree(original, work)
    ev = Evidence(project, work, out / project)
    error = None
    try:
        if entry["language"] == "Java":
            (work / "build").mkdir(exist_ok=True)
            files = sorted(str(p.relative_to(work)) for p in work.rglob("*.java"))
            ev.run(["javac", "-d", "build", *files], name="javac_compile")
            for file in entry["test_files"]:
                ev.run(["java", "-ea", "-cp", "build", Path(file).stem], name=Path(file).stem, kind="test_suite", strict=False)
        elif entry["language"] == "C#":
            (work / "global.json").write_text(json.dumps({"sdk": {"version": "8.0.426", "rollForward": "disable"}}))
            version = ev.run(["dotnet", "--version"], name="dotnet_sdk_version", kind="toolchain")
            if version["stdout"].strip() != "8.0.426":
                raise RuntimeError("Expected .NET SDK 8.0.426 in the temporary project copy")
            ev.run(["dotnet", "run", "--project", "tests/P042.Tests.csproj"], name="dotnet_assertion_suite", kind="test_suite", strict=False)
        elif (work / "run_tests.py").is_file():
            ev.run([sys.executable, "-B", "run_tests.py"], name="unittest_project_suite", kind="test_suite", timeout=900, strict=False)
        else:
            for file in entry["test_files"]:
                ev.run([sys.executable, "-B", file], name=Path(file).stem, kind="test_suite", strict=False)
        for file in entry["demo_files"]:
            ev.run([sys.executable, "-B", file], name="demo_" + Path(file).stem, kind="demo", timeout=300, strict=False)
        runtime = entry["runtime"]
        if runtime:
            if skip_runtime:
                ev.skip(runtime, "--skip-runtime requested; deployment was NOT verified")
            else:
                {"docker_api": docker_api, "compose_stack": compose_stack, "kubernetes_cluster": kubernetes_cluster}[runtime](ev)
    except Exception:
        error = traceback.format_exc()
        ev.record({"kind": "runner_exception", "name": "project_exception", "status": "FAIL", "traceback": error})
    after = tree_hashes(original)
    unchanged = before == after
    ev.record({"kind": "source_integrity", "name": "original_files_unchanged", "status": "PASS" if unchanged else "FAIL", "files": len(before),
               "changed": sorted(k for k in before.keys() | after.keys() if before.get(k) != after.get(k))})
    write_json(ev.out / "source_sha256_readonly_snapshot.json", before)
    counted = [r["unittest"] for r in ev.records if r.get("unittest")]
    suites = [r for r in ev.records if r["kind"] == "test_suite"]
    expected_suites = entry["expected_suite_processes"]
    runtime_checks = [r for r in ev.records if r["kind"] == "runtime_check" and r["status"] == "PASS"]
    coverage_ok = len(suites) == expected_suites and len(runtime_checks) == entry["expected_runtime_checks"]
    if entry["test_entrypoint"]:
        coverage_ok = coverage_ok and sum(r["tests_run"] for r in counted) > 0
    ev.record({"kind": "coverage", "name": "required_suites_and_runtime_checks", "status": "PASS" if coverage_ok else "INCOMPLETE",
               "suite_processes_expected": expected_suites, "suite_processes_executed": len(suites),
               "runtime_checks_expected": entry["expected_runtime_checks"], "runtime_checks_passed": len(runtime_checks)})
    bad = [r for r in ev.records if r["status"] in {"FAIL", "BLOCKED", "TIMEOUT", "INCOMPLETE", "SKIPPED"} and r["kind"] != "diagnostic"]
    report = {"project": project, "status": "PASS" if not bad and suites else "FAIL" if any(r["status"] == "FAIL" for r in bad) else "INCOMPLETE",
              "scope": entry["scope"], "runtime_required": entry["runtime"], "suite_count": len(suites),
              "suite_count_expected": expected_suites, "runtime_checks_expected": entry["expected_runtime_checks"],
              "suite_passed": sum(r["status"] == "PASS" for r in suites),
              "unittest_tests_run": sum(r["tests_run"] for r in counted),
              "unittest_failures": sum(r["failures"] for r in counted), "unittest_errors": sum(r["errors"] for r in counted),
              "unittest_skipped": sum(r["skipped"] for r in counted),
              "subcases_reported": sum(r["subcases"] or 0 for r in counted),
              "assertion_script_suite_count": sum(r.get("unittest") is None for r in suites),
              "count_note": "Unittest counts come from executed reports. Top-level Python/Java/C# assertion programs are suites, not a fabricated count of individual tests.",
              "runtime_checks": sum(r["kind"] == "runtime_check" for r in ev.records),
              "runtime_checks_passed": sum(r["kind"] == "runtime_check" and r["status"] == "PASS" for r in ev.records),
              "source_unchanged": unchanged, "steps": ev.records, "exception": error}
    write_json(ev.out / "results.json", report)
    return report


def parse_projects(value):
    chosen = set()
    for part in value.split(","):
        numbers = [int(s.removeprefix("P")) for s in part.split("-")]
        chosen.update(range(numbers[0], numbers[-1]+1))
    if not chosen or not chosen <= set(range(41, 81)):
        raise argparse.ArgumentTypeError("Choose projects in P041-P080 only")
    return sorted(chosen)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sources", type=Path, required=True, help="Directory containing projects/P041 ... P080")
    parser.add_argument("--out", type=Path, required=True, help="New output directory, outside source projects")
    parser.add_argument("--projects", type=parse_projects, default=list(range(41,81)))
    parser.add_argument("--skip-runtime", action="store_true", help="Explicitly INCOMPLETE for P054-P056; never a CI PASS")
    args = parser.parse_args()
    sources, out = args.sources.resolve(), args.out.resolve()
    if not (sources / "projects").is_dir():
        parser.error("--sources must contain projects/")
    if out == sources or out.is_relative_to(sources / "projects"):
        parser.error("--out must not be inside original projects/")
    out.mkdir(parents=True, exist_ok=True)
    matrix = json.loads((HERE / "matriceci.json").read_text())["projects"]
    entries = [e for e in matrix if int(e["project"][1:]) in args.projects]
    env = {"started_utc": datetime.now(timezone.utc).isoformat(), "python": sys.version,
           "executable": sys.executable, "platform": platform.platform(),
           "github_run_id": os.environ.get("GITHUB_RUN_ID"), "github_sha": os.environ.get("GITHUB_SHA"),
           "dependencies": {}}
    for package in ("numpy","scipy","scikit-learn","cryptography","fastapi","pydantic","uvicorn","httpx","psycopg","PyYAML","Pillow"):
        try: env["dependencies"][package] = importlib.metadata.version(package)
        except importlib.metadata.PackageNotFoundError: env["dependencies"][package] = None
    write_json(out / "environment.json", env)
    results = []
    for entry in entries:
        try:
            result = execute_project(entry, sources, out, args.skip_runtime)
        except Exception:
            result = {"project": entry["project"], "status": "BLOCKED", "traceback": traceback.format_exc()}
            write_json(out / entry["project"] / "results.json", result)
        results.append(result)
        write_json(out / "summary.json", {"projects_requested": len(entries), "projects": results,
                   "passed": sum(r["status"] == "PASS" for r in results),
                   "complete": len(results) == len(entries), "status": "PASS" if len(results)==len(entries) and all(r["status"]=="PASS" for r in results) else "INCOMPLETE_OR_FAILED"})
    return 0 if results and all(r["status"] == "PASS" for r in results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
