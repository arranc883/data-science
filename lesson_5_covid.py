import pandas as pd
import numpy as np
import plotly.graph_objects as go

#reading data
data=pd.read_csv('C:\\Users\\arran\\OneDrive\\Desktop\\data science\\files\\WHO-COVID-19-global-data.csv')

#basic info of data
print(data.info())

#printing row data types
print(data.dtypes)

#changing DateReported data type
data['DateReported']=pd.to_datetime(data['DateReported'])

#checking if it worked
print(data.dtypes)

#getting sum of groups of data reported
datawise=data.groupby('DateReported').sum()

#checking if it worked
print(datawise)

#####################
#####################
#####################

fig1=go.Figure()

fig1.add_trace(go.Scatter(x=datawise.index, y=datawise['Cumulative_cases'], fill='tonexty',  line_color='blue'))

fig1.update_layout(title='cumulative cases world wide')

fig1.write_html('fg1.html', auto_open=True)

#####################
#####################
#####################

fig2=go.Figure()

fig2.add_trace(go.Scatter(x=datawise.index, y=datawise['Cumulative_deaths'], fill='tonexty',  line_color='red',))

fig2.update_layout(title='cumulative deaths world wide')

fig2.write_html('fig2.html', auto_open=True)

########################
########################
########################

fig3=go.Figure()

fig3.add_trace(go.Scatter(x=datawise.index, y=datawise['New_cases'], fill='tonexty',  line_color='yellow',))

fig3.update_layout(title='New_cases world wide')

fig3.write_html('fig3.html', auto_open=True)

########################
########################
########################

fig4=go.Figure()

fig4.add_trace(go.Scatter(x=datawise.index, y=datawise['New_deaths'], fill='tonexty',  line_color='pink',))

fig4.update_layout(title='new deaths world wide')

fig4.write_html('fig4.html', auto_open=True)
