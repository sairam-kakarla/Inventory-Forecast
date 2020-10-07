import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

dataset=pd.read_csv('C:/Users/abhis/OneDrive/Documents/Programs/jan2020.csv')
date_f=pd.to_datetime(dataset.Date)

x=dataset[['Discount']]
y=dataset['Quantity']

x_train,x_test,y_train,y_test=train_test_split(x,y,train_size=0.8,test_size=0.01,random_state=10)

regressor=LinearRegression()
regressor.fit(x_train,y_train)

def predictor(p):
    v = pd.DataFrame({'value':[p]})
    predict=regressor.predict(v)
    df=pd.DataFrame({'Actual Quantity':y_test,'Predicted Quantity':predict})
    return predict