from fastapi import FastAPI, status, HTTPException
import uvicorn
from testapi.Fibo import Fibonacci
app = FastAPI()
list =[]
@app.get("/")
def root():
    return{"message: hello world"}

@app.get("/getitem/{n}")
def inp(n):
    try:
        a = int(n)
    except ValueError:
        raise HTTPException(status_code=422,detail='entry should be an integer')
    else:
        list.append(n)
        user_saved = Fibonacci(a)
        return user_saved

         

   
  
            

        
    
    
     
           
    
            
             


    

if __name__=='__main__':
    uvicorn.run(app)      