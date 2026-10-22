import sqlite3

def init_db(con):
    con.execute("CREATE TABLE IF NOT EXISTS item(id INTEGER PRIMARY KEY, name TEXT NOT NULL UNIQUE)")
    con.commit()

def add_item(con, name):
    name=name.strip()
    if not name: raise ValueError("name")
    con.execute("INSERT INTO item(name) VALUES (?)",(name,))
    con.commit()

def list_items(con):
    return con.execute("SELECT id,name FROM item ORDER BY id").fetchall()
