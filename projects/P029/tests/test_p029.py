import sqlite3
from pathlib import Path


def expect_integrity_error(connection, statement, parameters, reason):
    try:
        connection.execute(statement, parameters)
    except sqlite3.IntegrityError:
        return
    raise AssertionError(reason)


con = sqlite3.connect(":memory:")
schema = Path(__file__).resolve().parents[1] / "sql" / "p029_schema.sql"
con.executescript(schema.read_text())
con.execute("INSERT INTO room(code) VALUES ('101')")
con.execute("INSERT INTO room(code) VALUES ('102')")


def can_book(room, start, end):
    count = con.execute(
        """SELECT count(*) FROM booking
           WHERE room_id=? AND NOT(end_date<=? OR start_date>=?)""",
        (room, start, end),
    ).fetchone()[0]
    return count == 0


assert can_book(1, '2026-10-10', '2026-10-12')
con.execute("INSERT INTO booking VALUES (1,1,'2026-10-10','2026-10-12')")
assert not can_book(1, '2026-10-11', '2026-10-13')
assert can_book(1, '2026-10-12', '2026-10-14')

# Il rifiuto deve avvenire anche scrivendo direttamente nel database.
# Gli intervalli sono validi e la nuova chiave è libera: si prova il trigger.
expect_integrity_error(
    con,
    "INSERT INTO booking VALUES (2,1,'2026-10-11','2026-10-13')",
    (),
    "Il trigger INSERT deve rifiutare una prenotazione sovrapposta",
)
assert con.execute("SELECT count(*) FROM booking").fetchone()[0] == 1

# Il giorno di partenza può coincidere con l'arrivo della prenotazione seguente.
con.execute("INSERT INTO booking VALUES (2,1,'2026-10-12','2026-10-14')")
expect_integrity_error(
    con,
    "UPDATE booking SET start_date='2026-10-11' WHERE id=2",
    (),
    "Il trigger UPDATE deve rifiutare una modifica in conflitto",
)
assert con.execute("SELECT start_date,end_date FROM booking WHERE id=2").fetchone() == (
    '2026-10-12', '2026-10-14'
)

# Una riga non deve entrare in conflitto con se stessa durante un aggiornamento.
con.execute("UPDATE booking SET start_date='2026-10-10' WHERE id=1")
# Gli stessi giorni sono disponibili per una camera diversa.
con.execute("INSERT INTO booking VALUES (3,2,'2026-10-10','2026-10-12')")
assert con.execute("SELECT count(*) FROM booking").fetchone()[0] == 3
con.close()
print("P029: overlap booking PASS")
