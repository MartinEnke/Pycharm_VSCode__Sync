from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

# Initialize the FastAPI app
app = FastAPI()

# Define the data model for an item (task, product, etc.)
class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

# Example list of items (this could be a database in a real project)
items = [
    {"name": "item1", "description": "This is item 1", "price": 10.5, "tax": 1.2},
    {"name": "item2", "description": "This is item 2", "price": 20.0, "tax": 2.5},
]

# Endpoint to get the list of items
@app.get("/items/", response_model=List[Item])
def get_items():
    return items

# Endpoint to add a new item
@app.post("/items/", response_model=Item)
def create_item(item: Item):
    items.append(item.dict())
    return item
