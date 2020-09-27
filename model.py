import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import confusion_matrix,accuracy_score
import matplotlib.pyplot as plt

class model:
    def load_data(self,location):
        self.location=location
        self.dataset=pd.read_csv(self.location)
        self.dataset['Date']=pd.to_datetime(self.dataset.Date)
        self.x=self.dataset[['Day','Festival','Holiday','Discount']]
        self.y=self.dataset['Quantity']

    def predict_model(self,data):
        if data!=None:
            self.x_test=pd.DataFrame(data)
        self.predict_data=self.regressor.predict(self.x_test)
        self.data_frame=pd.DataFrame({'Actual Price':self.y_test,"Predicted Price":self.predict_data})
        print(self.data_frame)
        
            
    def train_model(self,split):
        self.regressor=LinearRegression()
        if split!=0:
            self.x_train,self.x_test,self.y_train,self.y_test=train_test_split(self.x,self.y,train_size=split,random_state=2)
        else:
            self.x_train=self.x
            self.y_train=self.y
        self.regressor.fit(self.x_train,self.y_train)
        LinearRegression(copy_X=True,fit_intercept=True,n_jobs=None,normalize=True)

if __name__=='__main__':
    model1=model()
    #file location 
    #model1.load_data()
    model1.train_model(0.9)
    model1.predict_model(None)











'''
predict=regressor.predict(x_test)
df=pd.DataFrame({'Actual Quantity':y_test,'Predicted Quantity':predict})
print(regressor.score(x_test,y_test))
'''