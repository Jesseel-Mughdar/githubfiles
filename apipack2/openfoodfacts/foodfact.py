import requests
import pandas as pd
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
def sec_func():
    i=0
    l=[]
    r = requests.get('https://world.openfoodfacts.org/brands.json')
    data = r.json()
    d = data['tags']
    df = pd.DataFrame(columns=['data_id','data_name','products','link'])

    for item in data['tags']:
        while(i<5):
            for i in range(0,5):
                l.append(d[i])
                i+=1
                        
        data_id = item['id']
        data_name = item['name']
        products = item['products']
        link = item['url']
        df=df.append({'data_id':data_id,'data_name':data_name ,'products':products,'link':link}, ignore_index=True)
        #df3= df.to_csv("foodfacts.csv",index=False)
    return(l)
