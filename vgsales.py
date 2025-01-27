import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt


data=pd.read_csv('C:\\Users\\arran\\OneDrive\\Desktop\\data science\\files\\vgsales.csv')
data.index=range(1,16599)






print(data.info())
print(data.isnull().sum())


data.dropna(inplace=True)


#location
print(data.loc[2])

#identification
print(data.iloc[2])


#rows/columns
print(data.shape)


#data types
print(data.dtypes)

#change data
data['Year']=data['Year'].astype(int)

#top ten publishers
ttna=data.groupby('Publisher')['NA_Sales'].sum().nlargest(10)
print(ttna)

#how many unique publishers
print(len(data['Publisher'].unique()))


#make own column
data['total_sales']=data[['NA_Sales','EU_Sales','JP_Sales','Other_Sales']].sum(axis=1)
print(data.head(10))

#total sales by each region
tser=data.groupby('Publisher')[['NA_Sales','EU_Sales','JP_Sales','Other_Sales']].sum()
ttp=tser.sum(axis=1).nlargest(10).index
ptt=tser.loc[ttp]
print(ttp)

regions=['NA_Sales','EU_Sales','JP_Sales','Other_Sales']


for i in regions:
    plt.bar(ptt.index,ptt[i],label=i)
plt.legend()
plt.show()

##################################################################
#which seler sells the most number of units globally and how much?
##################################################################
