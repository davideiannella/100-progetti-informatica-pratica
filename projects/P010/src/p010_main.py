import csv
import sqlite3

def transform(row):
    x = {'istat': row['istat'].strip(), 'nome': row['nome'].strip().title(), 'provincia': row['provincia'].strip().upper(), 'popolazione': int(row['popolazione'])}
    if not all((x[k] for k in ('istat', 'nome', 'provincia'))):
        raise ValueError('Campi identificativi vuoti')
    if x['popolazione'] < 0:
        raise ValueError('Popolazione negativa')
    return x

def load_rows(conn, rows):
    clean = [transform(row) for row in rows]
    with conn:
        conn.execute('CREATE TABLE IF NOT EXISTS comuni(\n            istat TEXT PRIMARY KEY NOT NULL,\n            nome TEXT NOT NULL, provincia TEXT NOT NULL,\n            popolazione INTEGER NOT NULL CHECK(popolazione>=0))')
        for x in clean:
            conn.execute('INSERT INTO comuni VALUES(?,?,?,?)\n                ON CONFLICT(istat) DO UPDATE SET\n                nome=excluded.nome, provincia=excluded.provincia,\n                popolazione=excluded.popolazione', (x['istat'], x['nome'], x['provincia'], x['popolazione']))

def extract_csv(path):
    with open(path, newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))
