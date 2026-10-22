import sqlite3,pathlib
con=sqlite3.connect(":memory:"); con.executescript((pathlib.Path(__file__).parents[1]/"sql"/"p027_schema.sql").read_text())
con.execute("INSERT INTO member(name) VALUES ('Luca')")
con.execute("INSERT INTO membership(member_id,starts_on,ends_on) VALUES (1,'2026-10-01','2026-12-31')")
con.execute("INSERT INTO class(name,capacity) VALUES ('Functional',20)")
con.execute("INSERT INTO attendance VALUES (1,1,'2026-10-15')")
assert con.execute("SELECT count(*) FROM attendance").fetchone()[0]==1
bad=False
try: con.execute("INSERT INTO membership(member_id,starts_on,ends_on) VALUES (1,'2026-12-01','2026-11-01')")
except sqlite3.IntegrityError: bad=True
assert bad
print("P027: palestra DB PASS")
