import datetime
from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional
import time


class Item(BaseModel):
  name: str
  description: Optional[str] = None  # Optionalは必要だったら追加する
  price: int
  tax: float =Field(default=1.1)

app = FastAPI()

@app.post("/item/")
async def create_item(item: Item):
  return {"message":f"{item.name}は税込価格{int(item.price * item.tax)}円です"}