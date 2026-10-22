PRAGMA foreign_keys=ON;
CREATE TABLE dim_date(date_key INTEGER PRIMARY KEY, day TEXT, month INTEGER, year INTEGER);
CREATE TABLE dim_product(product_key INTEGER PRIMARY KEY, sku TEXT, category TEXT);
CREATE TABLE dim_store(store_key INTEGER PRIMARY KEY, name TEXT, city TEXT);
CREATE TABLE fact_sales(date_key INTEGER REFERENCES dim_date(date_key),
                        product_key INTEGER REFERENCES dim_product(product_key),
                        store_key INTEGER REFERENCES dim_store(store_key),
                        qty INTEGER NOT NULL, revenue_cents INTEGER NOT NULL);
