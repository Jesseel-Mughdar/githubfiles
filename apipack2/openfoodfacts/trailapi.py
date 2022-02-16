import json
from textwrap import indent
import requests
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import pandas as pd
from fastapi import FastAPI
import uvicorn



i=0
l=[]

app = FastAPI()


@app.get("/")
def main_func():
    return{"Message: Success"}

   
@app.get('/home/')
def sec_func():
    r = requests.get('https://world.openfoodfacts.org/brands.json')
    data = r.json()
    d = data['tags']
    df = pd.DataFrame(columns=['data_id','data_name','products','link'])

    for item in data['tags']:
        global i
        while(i<5):
            for i in range(0,5):
                l.append(d[i])
                i+=1
                        
        data_id = item['id']
        data_name = item['name']
        products = item['products']
        link = item['url']
        df=df.append({'data_id':data_id,'data_name':data_name ,'products':products,'link':link}, ignore_index=True)
        df3= df.to_csv("foodfacts.csv",index=False)
    return(l)



uvicorn.run(app)
