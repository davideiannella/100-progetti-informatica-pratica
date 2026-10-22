import sqlite3, pathlib
con=sqlite3.connect(":memory:"); con.execute("PRAGMA foreign_keys=ON")
con.executescript((pathlib.Path(__file__).parents[1]/"sql"/"p026_schema.sql").read_text())
con.execute("INSERT INTO student(matricola,name) VALUES ('S1','Anna')")
con.execute("INSERT INTO course(code,title,credits) VALUES ('DB','Basi di dati',9)")
con.execute("INSERT INTO exam_session(course_id,exam_date) VALUES (1,'2026-11-10')")
con.execute("INSERT INTO registration VALUES (1,1)")
con.execute("INSERT INTO result VALUES (1,1,30,1)")
assert con.execute("SELECT grade,honors FROM result").fetchone()==(30,1)
bad=False
try: con.execute("INSERT INTO result VALUES (1,1,31,0)")
except sqlite3.IntegrityError: bad=True
assert bad
print("P026: carriera universitaria PASS")
