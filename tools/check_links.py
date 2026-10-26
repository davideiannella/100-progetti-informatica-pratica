#!/usr/bin/env python3
"""Check navigational Markdown links without changing historical logs or code."""
from pathlib import Path
from urllib.parse import unquote, urlsplit
import argparse, collections, json, re, unicodedata

REPO = Path(__file__).resolve().parents[1]
REPO_URL = 'https://github.com/davideiannella/100-progetti-informatica-pratica'

def markdown_links(text):
    fence = None
    for number, line in enumerate(text.splitlines(), 1):
        marker = re.match(r'^\s*(`{3,}|~{3,})', line)
        if marker:
            ch = marker[1][0]
            if fence is None: fence = ch
            elif fence == ch: fence = None
            continue
        if fence: continue
        for match in re.finditer(r'\]\(\s*(<[^>]+>|[^\s]+?)(?:\s+["\'][^"\']*["\'])?\)', line):
            yield number, match[1].strip('<>')
        match = re.match(r'^\s*\[[^\]]+\]:\s*(\S+)', line)
        if match: yield number, match[1].strip('<>')
        for match in re.finditer(r'<(https?://[^>]+)>', line):
            yield number, match[1]

def anchors(path):
    seen = collections.Counter(); result = set()
    for line in path.read_text(encoding='utf-8').splitlines():
        match = re.match(r'^#{1,6}\s+(.+?)\s*#*$',line)
        if not match: continue
        value = re.sub(r'\[([^\]]+)\]\([^)]*\)',r'\1',match[1])
        value = re.sub(r'<[^>]+>','',value).lower()
        value = ''.join(c for c in value if c.isalnum() or c in ' _-')
        value = value.replace(' ','-')
        suffix = seen[value]; seen[value] += 1
        result.add(value + (f'-{suffix}' if suffix else ''))
    return result

def check(root=REPO):
    checks=[]; external=set(); problems=[]
    for source in sorted(root.rglob('*.md')):
        if '.git' in source.parts:continue
        for line,url in markdown_links(source.read_text(encoding='utf-8')):
            parsed=urlsplit(url)
            if parsed.scheme in {'mailto','tel','data'}:continue
            if parsed.scheme or parsed.netloc:
                external.add(url)
                match=re.match(re.escape(REPO_URL)+r'/(?:blob|tree)/main/([^?#]+)',url)
                if not match:continue
                target=root/unquote(match[1])
            else:
                target=(source.parent/unquote(parsed.path)).resolve() if parsed.path else source
            item={'source':source.relative_to(root).as_posix(),'line':line,'url':url,'target':str(target.relative_to(root)) if target.is_relative_to(root) else str(target)}
            if not target.is_relative_to(root):item['error']='outside_repository'
            elif not target.exists():item['error']='missing_path'
            elif parsed.fragment:
                anchor_file=target/'README.md' if target.is_dir() else target
                fragment=unquote(parsed.fragment).removeprefix('user-content-')
                if anchor_file.suffix=='.md' and fragment not in anchors(anchor_file):item['error']='missing_anchor'
            item['status']='failed' if 'error' in item else 'ok'
            checks.append(item)
            if 'error' in item:problems.append(item)
    return {'relative_and_main_links':len(checks),'external_urls':sorted(external),'problems':problems,'checks':checks}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--report',type=Path);args=p.parse_args()
    result=check()
    if args.report:args.report.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='checks' and k!='external_urls'},ensure_ascii=False,indent=2))
    raise SystemExit(bool(result['problems']))
