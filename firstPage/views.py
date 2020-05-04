from django.shortcuts import render
import pandas as pd
confirmedGlobal=pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv',encoding='utf-8',na_values=None)
    
# Create your views here.

def index(request):
    df=confirmedGlobal[confirmedGlobal['Country/Region']=='India'].transpose().iloc[4:].reset_index()
    df.columns=['Dates','CumulatedValues']
    df['ActualValues']=df['CumulatedValues'] -df['CumulatedValues'].shift(1).fillna(0)
    allData=[]
    for i in range(df.shape[0]):
        temp=df.loc[i]
        allData.append(dict(temp))
    context= {'data':allData}
    return render(request,'index.html',context)
