
from fastapi import FastAPI, Response, status, HTTPException
import uvicorn
from typing import Optional
from pydantic import BaseModel
app =FastAPI()

class Items(BaseModel):
    name: Optional[str] = None
    age: Optional [int] =None
    location:Optional [int] =None
class UpdateItems(BaseModel):
    name:str
    age:int
    location:str    
inventory ={}
@app.get("/")
def home():
    return{'message: hello world'}

@app.get("/getitem/{item_id}")
def getitem(item_id:int):
        if item_id in inventory:
            return inventory[item_id] 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)        

@app.post("/create/{item_id}")
def create(item_id:int, item:Items):
    if item_id in inventory:
        raise HTTPException(status_code=409, detail= " item already exist")
    inventory[item_id]=item
    
    return inventory[item_id]   
@app.put("/update/{item_id}")
def update(item_id:int, item:UpdateItems):
    if item_id not in inventory:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)  
    if item.name!= None:
        inventory[item_id].name = item.name
    if item.age!= None:
        inventory[item_id].age = item.age
    if item.name!= None:
        inventory[item_id].location = item.location 
             
    return inventory[item_id] 
@app.delete("/deleteitem")
def delete (item_id:int):
    if item_id not in inventory:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)  
    del inventory[item_id]
    return{"Sucess: item deleted"}    

    

    




uvicorn.run(app)    
