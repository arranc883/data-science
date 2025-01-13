import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

#read data 
data=pd.read_csv('C:\\Users\\arran\\OneDrive\\Desktop\\data science\\files\\adult.csv')

data.columns=data.columns.str.strip()

#add 
data.columns=['age','employment_type','wieght','education','years_education','married','designation','relationship','ethinicity','gender','capital_gains','capital_loss','working_hours','country','income']

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
data.drop(['wieght','capital_gains','capital_loss','country'],axis=1, inplace=True)

#printing data types
print(data.dtypes)

#converting cat data into int data
data['gender']=data['gender'].map({'Male':0 ,'Female':1}).astype(int)

#checkng if it worked
print(data['gender'].head())
