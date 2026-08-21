from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class StockPayload(BaseModel):
    item_id: str
    quantity: int
    location: str

@app.get("/")
def read_root():
    return {"message": "API is online"}

@app.post("/webhooks/warehouse-stock")
def warehouse_stock(payload: StockPayload):
    return {"status": "received", "data": payload}

