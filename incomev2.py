import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

#read data 
data=pd.read_csv('C:\\Users\\arran\\OneDrive\\Desktop\\data science\\files\\adult.csv')

data.columns=data.columns.str.strip()

#add 
data.columns=['age','employment_type','weight','education','years_education','married','designation','relationship','ethinicity','gender','capital_gains','capital_loss','working_hours','country','income']

#basic descripton of data
print(data.describe())

#check basic info
print(data.info())

#check for sum of null data (0)
print(data.isnull().sum()) 

#value counts of all the data
for i in data.columns:
    print(data[i].value_counts())

#droping unrequired columns
data.drop(['weight','capital_gains','capital_loss','country'],axis=1, inplace=True)

#printing data types
print(data.dtypes)

data['employment_type']=data['employment_type'].replace(' ?',np.nan)
data['designation']=data['designation'].replace('  ?',np.nan)
data.dropna(inplace=True)
print(data.isnull().sum())


#stripping spaces in data
#for i in data.columns:
 #  data[i]=data[i].str.strip()

#converting cat data into int data
data['gender']=data['gender'].map({' Male':0 ,' Female':1}).astype(int)
data['married']=data['married'].map({' Never-married':0 ,' Married-civ-spouse':1, ' Divorced':2, ' Separated':3 , ' Widowed':4 ,' Married-spouse-absent':5 , ' Married-AF-spouse':6 }).astype(int)
data['income']=data['income'].map({' <=50K':0 ,' >50K':1}).astype(int)
data['education']=data['education'].map({' HS-grad':0 ,' Some-college':1,  ' Bachelors':2 ,  ' Masters':3 , ' Assoc-voc':4  , ' 11th':5, ' Assoc-acdm':6  ,' 10th':7  , ' 7th-8th':8 , ' Prof-school':9, ' 9th':10 , ' 12th':11  ,  ' Doctorate':12 , ' 5th-6th':13 , ' 1st-4th':14  , ' Preschool':15}).astype(int)

#not computable data
#data['employment_type']=data['employment_type'].map({' Private':0 ,' Self-emp-not-inc':1,' Local-gov':2,  ' State-gov':3  , ' Self-emp-inc':4 ,' Federal-gov':5,' Without-pay' :6, ' Never-worked':7}).astype(int)
#data['designation']=data['designation'].map({' Prof-specialty':0 ,'Craft-repair':1,  'Exec-managerial':2 ,  'Adm-clerical':3 , 'Sales':4  , 'Other-service':5, 'Assoc-acdm':6  ,'Machine-op-inspct':7  , '?':8 , 'Transport-moving':9, 'Handlers-cleaners ':10 , 'Farming-fishing':11  ,  'Tech-support':12 , 'Protective-serv':13 , 'Priv-house-serv ':14  , 'Armed-Forces':15}).astype(int)

#checkng if it worked
print(data['gender'].head())

data.groupby('education').income.mean().plot(kind='bar')
plt.show()

