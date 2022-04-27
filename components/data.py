import pandas_datareader.data as web
import pandas_datareader.nasdaq_trader as nasdaq
import pandas as pd


company_name=nasdaq.get_nasdaq_symbols()['Security Name']

options=[]

for ticker in company_name.index:
    mydict={}
    mydict['label']=company_name[company_name.index.str.contains(ticker)]
    mydict['valuel']=ticker
    options.append(mydict)