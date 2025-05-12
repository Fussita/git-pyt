
from typing import Annotated, Union
from _codes.fastapi import FastAPI, Query
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

class ItemResponse(BaseModel): 
    name: str 
    price: float 

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hola": "Mundo"}
 
# http://127.0.0.1:8000/docs
# http://127.0.0.1:8000/redoc
# http://127.0.0.1:8000/items/5?q=somequery   
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.post("/items/{item_id}", response_model=ItemResponse)
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

k = f'Pizza{p}'

@app.get("/rococo/") 
async def read_items( 
    q: Annotated[ 
        str | None, 
        Query( 
            title="Query string", 
            description="Query string for the items to search in the database that have a good match", 
            min_length=3, 
            max_length=50, 
            pattern="^fixedquery$" # Ejemplo de regex 
        ) 
    ] = None 
): 
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]} 
    if q: 
        results.update({"q": q}) 
    return results 

