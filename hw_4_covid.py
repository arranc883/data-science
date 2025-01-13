import pandas as pd
import numpy as np


import plotly
import plotly.express as px
import plotly.graph_objects as go

data=pd.read_csv('C:\\Users\\arran\\OneDrive\\Desktop\\data science\\files\\covid_data.csv')

data=data[['Province_State','Country_Region','Confirmed','Recovered','Deaths','Active']]


usas=data['Country_Region']=='US'
usas=data[usas].nlargest(5,'Confirmed')
print(usas)


usas=data['Country_Region']=='US'
usas=data[usas].nlargest(5,'Deaths')
print(usas)



nda=data['Country_Region']=='India'
nda=data[nda].nlargest(5,'Confirmed')
print(nda)


nda=data['Country_Region']=='India'
nda=data[nda].nlargest(5,'Deaths')
print(nda)



fig4=go.Figure(data=[go.Bar(name='confirmed cases us', x=usas['Province_State'], y=usas['Confirmed']),
                     go.Bar(name='confirmed deaths us', x=usas['Province_State'], y=usas['Deaths']),
                     go.Bar(name='confirmed cases india', x=nda['Province_State'], y=nda['Confirmed']),
                     go.Bar(name='confirmed deaths india', x=nda['Province_State'], y=nda['Deaths'])])


fig4.update_layout(title='most affected states in the usa', barmode='stack', height=600)
fig4.write_html('fig4.html', auto_open=True)
