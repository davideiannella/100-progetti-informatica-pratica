import sqlite3
from pathlib import Path


def expect_integrity_error(connection, statement, parameters, reason):
    try:
        connection.execute(statement, parameters)
    except sqlite3.IntegrityError:
        return
    raise AssertionError(reason)


con = sqlite3.connect(":memory:")
schema = Path(__file__).resolve().parents[1] / "sql" / "p030_schema.sql"
con.executescript(schema.read_text())
con.execute("INSERT INTO book(title) VALUES ('Reti')")
con.execute("INSERT INTO book(title) VALUES ('Database')")
con.execute("INSERT INTO member(name) VALUES ('Anna')")
con.execute("INSERT INTO loan VALUES (1,1,1,'2026-10-01','2026-10-15',NULL)")
assert con.execute("SELECT count(*) FROM active_loans").fetchone()[0] == 1

# Il libro 2 non ha prestiti: il rifiuto deve dipendere dalle date,
# senza essere mascherato dall'indice che vieta due prestiti attivi.
expect_integrity_error(
    con,
    "INSERT INTO loan VALUES (2,2,1,'2026-10-20','2026-10-10',NULL)",
    (),
    "Il trigger INSERT deve rifiutare una scadenza precedente al prestito",
)
assert con.execute("SELECT count(*) FROM loan").fetchone()[0] == 1

expect_integrity_error(
    con,
    "UPDATE loan SET due_on='2026-09-30' WHERE id=1",
    (),
    "Il trigger UPDATE deve rifiutare una scadenza precedente al prestito",
)
assert con.execute("SELECT due_on FROM loan WHERE id=1").fetchone()[0] == '2026-10-15'

# Le date sono valide: qui si controlla separatamente l'unicità del prestito attivo.
expect_integrity_error(
    con,
    "INSERT INTO loan VALUES (2,1,1,'2026-10-02','2026-10-16',NULL)",
    (),
    "Lo stesso esemplare non può avere due prestiti attivi",
)

# La restituzione libera l'esemplare, senza cancellare il prestito dallo storico.
con.execute("UPDATE loan SET returned_on='2026-10-05' WHERE id=1")
assert con.execute("SELECT count(*) FROM active_loans").fetchone()[0] == 0
assert con.execute("SELECT count(*) FROM loan").fetchone()[0] == 1
con.execute("INSERT INTO loan VALUES (2,1,1,'2026-10-06','2026-10-20',NULL)")
assert con.execute("SELECT id FROM active_loans").fetchall() == [(2,)]
assert con.execute("SELECT count(*) FROM loan").fetchone()[0] == 2
con.close()
print("P030: view + trigger PASS")
