import sqlite3,pathlib
con=sqlite3.connect(":memory:"); con.execute("PRAGMA foreign_keys=ON")
con.executescript((pathlib.Path(__file__).parents[1]/"sql"/"p028_schema.sql").read_text())
con.execute("INSERT INTO product(sku,name,stock,price_cents) VALUES ('A','SSD',5,9900)")
con.execute("INSERT INTO customer_order DEFAULT VALUES")
con.commit()
con.execute("BEGIN")
stock=con.execute("SELECT stock FROM product WHERE id=1").fetchone()[0]
qty=2
assert stock>=qty
con.execute("UPDATE product SET stock=stock-? WHERE id=1",(qty,))
con.execute("INSERT INTO order_line VALUES (1,1,?,9900)",(qty,))
con.execute("COMMIT")
assert con.execute("SELECT stock FROM product").fetchone()[0]==3
assert con.execute("SELECT qty FROM order_line").fetchone()[0]==2
print("P028: transazione ordine/magazzino PASS")
