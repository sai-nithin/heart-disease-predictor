import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
dataa = pd.read_csv('pro.csv')
features=["age","sex","cp","trestbps","chol","fbs","restecg","thalach","exang","oldpeak","slope","ca","thal"]
lol=["target"]
x=dataa[features]
y=dataa[lol]
from sklearn.model_selection import train_test_split            
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)
from sklearn.tree import DecisionTreeClassifier
dtc= DecisionTreeClassifier(criterion='entropy',random_state=5)
dtc.fit(x_train,y_train)
pickle.dump(dtc, open('model.pkl', 'wb'))
model = pickle.load(open('model.pkl', 'rb'))