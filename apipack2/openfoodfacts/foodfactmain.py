from fastapi import FastAPI
import uvicorn
import foodfactapi

app = FastAPI()
@app.get("/")
def main_func():
    return{"Message: Success"} 
@app.get('/home/')
def inp():
    a = foodfactapi.api_call()
    return a

uvicorn.run(app)
