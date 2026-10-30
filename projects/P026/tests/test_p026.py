import sqlite3
from pathlib import Path


def expect_integrity_error(connection, statement, parameters, reason):
    try:
        connection.execute(statement, parameters)
    except sqlite3.IntegrityError:
        return
    raise AssertionError(reason)


con = sqlite3.connect(":memory:")
schema = Path(__file__).resolve().parents[1] / "sql" / "p026_schema.sql"
con.executescript(schema.read_text())
con.execute("INSERT INTO student(matricola,name) VALUES ('S1','Anna')")
con.execute("INSERT INTO course(code,title,credits) VALUES ('DB','Basi di dati',9)")
con.execute("INSERT INTO exam_session(course_id,exam_date) VALUES (1,'2026-11-10')")
con.execute("INSERT INTO exam_session(course_id,exam_date) VALUES (1,'2026-12-10')")
con.execute("INSERT INTO registration VALUES (1,1)")

# I voti validi vengono provati separatamente, senza duplicare la chiave.
for grade, honors in [(18, 0), (30, 1)]:
    con.execute("INSERT INTO result VALUES (1,1,?,?)", (grade, honors))
    assert con.execute("SELECT grade,honors FROM result").fetchone() == (grade, honors)
    con.execute("DELETE FROM result")

# La tabella resta vuota: ogni rifiuto dipende dal vincolo in esame,
# non dalla presenza di un risultato precedente per lo stesso appello.
for grade, honors, reason in [
    (17, 0, "Un voto inferiore a 18 deve essere rifiutato"),
    (31, 0, "Un voto superiore a 30 deve essere rifiutato"),
    (29.5, 0, "Un voto frazionario deve essere rifiutato"),
    (29, 1, "La lode richiede il voto 30"),
    (30, 2, "La lode deve essere rappresentata da 0 oppure 1"),
]:
    expect_integrity_error(
        con, "INSERT INTO result VALUES (1,1,?,?)", (grade, honors), reason
    )
    assert con.execute("SELECT count(*) FROM result").fetchone()[0] == 0

# L'appello 2 esiste, ma lo studente non è iscritto a quell'appello.
expect_integrity_error(
    con,
    "INSERT INTO result VALUES (1,2,30,0)",
    (),
    "Un risultato richiede la corrispondente iscrizione",
)

# Il controllo dei duplicati è distinto dai controlli sul voto e sulla lode.
con.execute("INSERT INTO result VALUES (1,1,30,1)")
expect_integrity_error(
    con,
    "INSERT INTO result VALUES (1,1,18,0)",
    (),
    "Non sono ammessi due risultati per la stessa iscrizione",
)
assert con.execute("SELECT grade,honors FROM result").fetchall() == [(30, 1)]
con.close()
print("P026: carriera universitaria PASS")
