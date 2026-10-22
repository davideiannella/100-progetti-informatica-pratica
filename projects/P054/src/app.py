from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, field_validator

app = FastAPI(title="P054 Items API", version="1.0")
items: dict[int, dict] = {}

class ItemIn(BaseModel):
    name: str = Field(min_length=1, max_length=80)
    quantity: int = Field(strict=True, ge=0, le=100000)

    @field_validator("name")
    @classmethod
    def nonblank(cls, value):
        value = value.strip()
        if not value:
            raise ValueError("name vuoto")
        return value

@app.get("/health")
def health():
    return {"status":"ok"}

@app.post("/items/{item_id}")
def upsert_item(item_id: int, item: ItemIn):
    if item_id <= 0:
        raise HTTPException(status_code=400, detail="item_id must be positive")
    items[item_id]=item.model_dump()
    return {"id":item_id, **items[item_id]}

@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id <= 0:
        raise HTTPException(status_code=400, detail="item_id must be positive")
    if item_id not in items:
        raise HTTPException(status_code=404, detail="not found")
    return {"id":item_id, **items[item_id]}
