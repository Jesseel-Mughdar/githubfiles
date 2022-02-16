from fastapi import FastAPI
import uvicorn
import foodfact

app = FastAPI()
@app.get("/")
def main_func():
    return{"Message: Success"} 
@app.get('/home/')
def inp():
    a = foodfact.api_call()
    return a

uvicorn.run(app)
