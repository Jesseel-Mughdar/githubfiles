from fastapi import FastAPI
import uvicorn
from testapi.Fibo import Fibonacci
app = FastAPI()
list =[]
@app.get("/")
def root():
    return{"message: hello world"}

@app.get("/getitem/{n}")
def inp(n:int):
    for i in range(0, len(list)):
        if i==n:
            return{'item not found'}   
           
        else:
            user_saved = Fibonacci(n)
            return user_saved
             

     
@app.post("/putitem/{n}")
def get_data(n:int):
    list.append(n)
    return list

if __name__=='__main__':
    uvicorn.run(app)      