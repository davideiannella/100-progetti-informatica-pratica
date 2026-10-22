import sqlite3, pathlib
sql=(pathlib.Path(__file__).parents[1]/"sql"/"p025_schema.sql").read_text()
con=sqlite3.connect(":memory:"); con.executescript(sql)
con.execute("INSERT INTO patient(code) VALUES ('P001')")
con.execute("INSERT INTO doctor(name) VALUES ('Rossi')")
con.execute("INSERT INTO service(name,duration_min) VALUES ('Visita',30)")
con.execute("INSERT INTO slot(doctor_id,service_id,starts_at) VALUES (1,1,'2026-10-20T09:00')")
con.execute("INSERT INTO booking(patient_id,slot_id) VALUES (1,1)")
assert con.execute("SELECT count(*) FROM booking").fetchone()[0]==1
ok=False
try: con.execute("INSERT INTO booking(patient_id,slot_id) VALUES (1,1)")
except sqlite3.IntegrityError: ok=True
assert ok
print("P025: booking constraints PASS")
