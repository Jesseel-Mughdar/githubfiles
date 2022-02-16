from fastapi import FastAPI
import uvicorn
import foodfact




app = FastAPI()


@app.get("/")
def main_func():
    return{"Message: Success"}

   
@app.get('/home/')
def inp():
    a = foodfact.sec_func()
    return a





uvicorn.run(app)
