from fastapi import FastAPI
import json

app = FastAPI()
DB_PATH = "/app/db/shopping_list.json"

@app.get("/items")
def get_items():
    try:
        with open(DB_PATH, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

@app.post("/items")
def add_item(name: str, amount: int):
    with open(DB_PATH, "r") as f:
        items = json.load(f)    
    new_id = len(items) + 1
    new_item = {"id": new_id, "name": name, "amount": amount}
    items.append(new_item)

    with open(DB_PATH, "w") as f:
        json.dump(items, f)   
    return new_item