import sqlite3,pathlib
con=sqlite3.connect(":memory:")
con.executescript((pathlib.Path(__file__).parents[1]/"sql"/"p035_schema.sql").read_text())
con.execute("INSERT INTO account(username,role) VALUES ('alice','reader')")
con.execute("INSERT INTO document(title,body) VALUES ('Policy','v1')")
con.execute("UPDATE document SET body='v2' WHERE id=1")
acts=[r[0] for r in con.execute("SELECT action FROM audit_log ORDER BY id")]
assert acts==["INSERT","UPDATE"]
bad=False
try: con.execute("INSERT INTO account(username,role) VALUES ('x','root')")
except sqlite3.IntegrityError: bad=True
assert bad
print("P035: audit trigger + role domain PASS")
