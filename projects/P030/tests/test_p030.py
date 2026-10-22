import sqlite3,pathlib
con=sqlite3.connect(":memory:"); con.executescript((pathlib.Path(__file__).parents[1]/"sql"/"p030_schema.sql").read_text())
con.execute("INSERT INTO book(title) VALUES ('Reti')")
con.execute("INSERT INTO member(name) VALUES ('Anna')")
con.execute("INSERT INTO loan(book_id,member_id,borrowed_on,due_on) VALUES (1,1,'2026-10-01','2026-10-15')")
assert con.execute("SELECT count(*) FROM active_loans").fetchone()[0]==1
bad=False
try: con.execute("INSERT INTO loan(book_id,member_id,borrowed_on,due_on) VALUES (1,1,'2026-10-20','2026-10-10')")
except sqlite3.IntegrityError: bad=True
assert bad
print("P030: view + trigger PASS")
