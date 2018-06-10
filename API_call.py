import pandas as pd
import matplotlib.pyplot as plt
import requests
import json
import urllib

def call_api(ticker, field, from_date, to_date):
    url_call = 'http://michelaa.pythonanywhere.com/stockdatareaderapi/'+ticker.upper()+'/'+field+'/'+from_date+'/'+to_date+'/'
    r = requests.get(url_call)
    rr = json.loads(r.content)
    return rr

def  datareader_doc():
    """ function to return the string 'my first package' """
    return("IE GMBD 2017 Group A first package that anyone can install it! The purpose of the package is to read the technology stock prices between 2 dates")
    
ticker = 'ATT'
field = 'Price_Sales'
from_date='20180406'
to_date='20180606'

try:
    df = pd.DataFrame(call_api(ticker,field,from_date,to_date))
    #print(df.head)
    if df.empty:
        print("Ticker or date values are not found!!!")
    else:
        plt.title(ticker+" "+field.replace('_','/')+" vs date")
        plt.plot(df['Price'])
        plt.ylabel('Price')
        plt.xlabel('Date')
        #plt.xticks(range(1,len(df['Dates'])), df['Dates'])
        plt.grid(True)
        plt.show()
    
except Exception as e:
    print(e)