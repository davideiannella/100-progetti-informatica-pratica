import sys, pathlib
sys.path.append(str(pathlib.Path(__file__).parents[1]/"src"))
from web_journey import journey

https = [x[0] for x in journey("https://example.test/index.html")]
http = [x[0] for x in journey("http://example.test/")]
assert https == ["URL","DNS","IP","TCP","TLS","HTTP","RESPONSE","CACHE"]
assert "TLS" not in http
bad=False
try: journey("example.test")
except ValueError: bad=True
assert bad
print("P047: web journey state model PASS")
