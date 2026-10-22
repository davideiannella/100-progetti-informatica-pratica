import sqlite3,pathlib
con=sqlite3.connect(":memory:"); con.executescript((pathlib.Path(__file__).parents[1]/"sql"/"p029_schema.sql").read_text())
con.execute("INSERT INTO room(code) VALUES ('101')")
def can_book(room,start,end):
    n=con.execute("""SELECT count(*) FROM booking
                     WHERE room_id=? AND NOT(end_date<=? OR start_date>=?)""",(room,start,end)).fetchone()[0]
    return n==0
assert can_book(1,'2026-10-10','2026-10-12')
con.execute("INSERT INTO booking(room_id,start_date,end_date) VALUES (1,'2026-10-10','2026-10-12')")
assert not can_book(1,'2026-10-11','2026-10-13')
assert can_book(1,'2026-10-12','2026-10-14')
print("P029: overlap booking PASS")
