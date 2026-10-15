import pandas as pd   
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split    
df = pd.read_csv("E:\\R & D\\project\\First VScode with python\\file concept\\flavors_of_cocoa.csv");
dataset=print(df);
X=df.iloc[1:20]; 
y=df.iloc[1:5]
X_train,y_train,X_test,y_test=train_test_split(X,y,test_size=0.2,random_state=0);
print(X_train);
print(X_test);
print(y_train);
print(y_train);
