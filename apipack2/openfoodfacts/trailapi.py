from unicodedata import name
import requests
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import pandas as pd
from fastapi import FastAPI
import uvicorn



#data = main_func(url)

app = FastAPI()


@app.get("/")
def main_func():
    return{"Message: Success"}

   
@app.get('/home/')
def sec_func():
    r = requests.get('https://world.openfoodfacts.org/brands.json')
    data = r.json()
    df = pd.DataFrame(columns=['data_id','data_name','products','link'])

    for item in data['tags']:
        data_id = item['id']
        data_name = item['name']
        products = item['products']
        link = item['url']
        df=df.append({'data_id':data_id,'data_name':data_name ,'products':products,'link':link}, ignore_index=True)
    df2=df.to_csv(index=False)
    return(df2)   




uvicorn.run(app)
