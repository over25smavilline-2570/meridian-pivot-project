from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3

app = FastAPI()


class StockWebhookPayload(BaseModel):
    sku: str
    size: str
    quantity: int
    event_type: str  # e.g., "stock_received" or "order_shipped"


@app.post("/webhooks/warehouse-stock")
def receive_stock_update(payload: StockWebhookPayload):
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()
    
    # Real-time stock update
    cursor.execute("""
        UPDATE inventory 
        SET quantity = ?, restock_date = NULL
        WHERE sku = ? AND size = ?
    """, (payload.quantity, payload.sku, payload.size))
    
    conn.commit()
    conn.close()
    
    return {"status": "success", "updated_sku": payload.sku}
