"""Query parametrizzate su un vero database SQLite locale, senza rete."""
import sqlite3


def make_db():
    con = sqlite3.connect(":memory:")
    with con:
        con.execute("CREATE TABLE user(id INTEGER PRIMARY KEY, username TEXT NOT NULL UNIQUE, role TEXT NOT NULL)")
        con.executemany("INSERT INTO user(username,role) VALUES (?,?)",
                        [("anna", "user"), ("mario", "admin")])
    return con


def find_user(con, username):
    if not isinstance(username, str):
        raise TypeError("username deve essere testo")
    if len(username) > 128:
        raise ValueError("username oltre 128 caratteri")
    # Il placeholder rappresenta un valore, non un nome tabella o un frammento SQL.
    return con.execute("SELECT username,role FROM user WHERE username=?", (username,)).fetchone()


def demo():
    con = make_db()
    try:
        print("Ricerca anna:", find_user(con, "anna"))
        print("Ricerca metacaratteri:", find_user(con, "' OR 1=1 --"))
        print("Utenti ancora presenti:", con.execute("SELECT count(*) FROM user").fetchone()[0])
    finally:
        con.close()


if __name__ == "__main__":
    demo()
