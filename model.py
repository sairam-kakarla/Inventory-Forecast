import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import confusion_matrix,accuracy_score
import matplotlib.pyplot as plt
dataset=pd.read_csv('S:/materials/fall2020/cse2003/project/2003proj/jan2020.csv')
dataset['Date']=pd.to_datetime(dataset.Date)
x=dataset[['Day','Festival','Holiday','Discount']]
y=dataset['Quantity']
x_train,x_test,y_train,y_test=train_test_split(x,y,train_size=0.2,random_state=2)
regressor=LinearRegression()
regressor.fit(x_train,y_train)
LinearRegression(copy_X=True,fit_intercept=True,n_jobs=None,normalize=False)
predict=regressor.predict(x_test)
df=pd.DataFrame({'Actual Quantity':y_test,'Predicted Quantity':predict})
print(regressor.score(x_test,y_test))
df.plot(kind='bar')
plt.show()