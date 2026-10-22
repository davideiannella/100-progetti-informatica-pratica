PRAGMA foreign_keys=ON;
CREATE TABLE product(id INTEGER PRIMARY KEY, sku TEXT UNIQUE NOT NULL, name TEXT NOT NULL, stock INTEGER NOT NULL CHECK(typeof(stock)='integer' AND stock>=0), price_cents INTEGER NOT NULL CHECK(typeof(price_cents)='integer' AND price_cents>=0));
CREATE TABLE customer_order(id INTEGER PRIMARY KEY, status TEXT NOT NULL DEFAULT 'CREATED');
CREATE TABLE order_line(order_id INTEGER NOT NULL REFERENCES customer_order(id), product_id INTEGER NOT NULL REFERENCES product(id),
                        qty INTEGER NOT NULL CHECK(typeof(qty)='integer' AND qty>0), price_cents INTEGER NOT NULL CHECK(typeof(price_cents)='integer' AND price_cents>=0),
                        PRIMARY KEY(order_id,product_id));
CREATE TABLE payment(id INTEGER PRIMARY KEY, order_id INTEGER NOT NULL UNIQUE REFERENCES customer_order(id),
                     amount_cents INTEGER NOT NULL CHECK(typeof(amount_cents)='integer' AND amount_cents>=0), status TEXT NOT NULL);
