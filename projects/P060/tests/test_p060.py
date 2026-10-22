import pathlib,subprocess,sys,json
root=pathlib.Path(__file__).parents[1]
wf=(root/".github"/"workflows"/"ci.yml").read_text()
assert "permissions:" in wf and "contents: read" in wf
assert "python -m unittest" in wf
r=subprocess.run([sys.executable,"build_release.py"],cwd=root,capture_output=True,text=True)
assert r.returncode==0,r.stderr
m=json.loads((root/"release_manifest.json").read_text())
assert len(m["sha256"])==64 and (root/m["artifact"]).exists()
print("P060: local CI gates + artifact hash PASS")
