import sqlite3,pathlib
con=sqlite3.connect(":memory:"); con.executescript((pathlib.Path(__file__).parents[1]/"sql"/"p033_schema.sql").read_text())
con.execute("INSERT INTO dim_date VALUES (20261001,'2026-10-01',10,2026)")
con.execute("INSERT INTO dim_product VALUES (1,'A','Storage')")
con.execute("INSERT INTO dim_store VALUES (1,'Store Roma','Roma')")
con.executemany("INSERT INTO fact_sales VALUES (20261001,1,1,?,?)",[(2,20000),(1,10000)])
row=con.execute("SELECT sum(qty),sum(revenue_cents) FROM fact_sales").fetchone()
assert row==(3,30000)
print("P033: star schema aggregation PASS")
