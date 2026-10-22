from contextlib import asynccontextmanager
import os
import psycopg
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, field_validator

def connect():
    return psycopg.connect(os.environ["DATABASE_URL"], connect_timeout=3)

@asynccontextmanager
async def lifespan(app):
    with connect() as con:
        con.execute("CREATE TABLE IF NOT EXISTS item(id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY, name TEXT NOT NULL UNIQUE)")
    yield

app = FastAPI(lifespan=lifespan)

class Item(BaseModel):
    name: str = Field(min_length=1, max_length=80)

    @field_validator("name")
    @classmethod
    def nonblank(cls, value):
        value = value.strip()
        if not value:
            raise ValueError("blank name")
        return value

@app.get("/health")
def health():
    try:
        with connect() as con:
            con.execute("SELECT 1").fetchone()
        return {"status": "ok"}
    except psycopg.Error as exc:
        raise HTTPException(503, "database unavailable") from exc

@app.get("/items")
def items():
    with connect() as con:
        return [{"id": row[0], "name": row[1]} for row in con.execute("SELECT id,name FROM item ORDER BY id")]

@app.post("/items", status_code=201)
def add(item: Item):
    try:
        with connect() as con:
            row = con.execute("INSERT INTO item(name) VALUES (%s) RETURNING id,name", (item.name,)).fetchone()
        return {"id": row[0], "name": row[1]}
    except psycopg.errors.UniqueViolation as exc:
        raise HTTPException(409, "duplicate") from exc
