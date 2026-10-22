from pathlib import Path
import json, sys
sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))
import os, tempfile
from itertools import product
from collections import Counter
from hardening_audit import CONFIG_KEYS, audit_config, audit_file, audit_mode
modes=[]
with tempfile.TemporaryDirectory(prefix="p069-documentazione-") as temp:
    path=Path(temp)/"segreto.conf"
    path.write_text("dato sintetico",encoding="utf-8")
    for mode in (0o600,0o644,0o606,0o777):
        os.chmod(path,mode)
        before=path.stat().st_mode
        findings=audit_file(path)
        modes.append({"mode":format(mode,"04o"),"findings":findings,"mode_unchanged":path.stat().st_mode==before,"content_unchanged":path.read_text()=="dato sintetico"})
    link=Path(temp)/"collegamento"
    link.symlink_to(path)
    symlink_findings=audit_file(link)
secure=dict(zip(CONFIG_KEYS,(False,False,True)))
configurations=[]
for values in product((False,True),repeat=3):
    cfg=dict(zip(CONFIG_KEYS,values)); configurations.append({"configuration":cfg,"findings":audit_config(cfg)})
counts=Counter(f for mode in range(0o10000) for f in audit_mode(mode))
try:
    audit_config({"password_authentication":"no"})
except ValueError as exc:
    invalid={"status":"RIFIUTATO","reason":str(exc)}
else:
    raise AssertionError("stringa accettata")
result={"files":modes,"symlink_findings":symlink_findings,"secure_config":secure,"secure_findings":audit_config(secure),
        "incomplete_findings":audit_config({"password_authentication":False}),"configurations":configurations,
        "permission_modes":4096,"finding_occurrences":dict(counts),"invalid_config":invalid}
assert modes[0]["findings"]==[] and modes[1]["findings"]==["group-readable","world-readable"]
assert all(r["mode_unchanged"] and r["content_unchanged"] for r in modes)
print(json.dumps(result,ensure_ascii=False,indent=2))
