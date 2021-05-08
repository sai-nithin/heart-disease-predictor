import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
dataa = pd.read_csv('pro.csv')
#print(dataa)
x=dataa.iloc[:,0:13]
#print(x)
y=dataa.iloc[:,-1:]
#print(y)
from sklearn.model_selection import train_test_split            
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
#x_train = sc.fit_transform(x_train)
#x_test = sc.transform(x_test)
from sklearn.tree import DecisionTreeClassifier
dtc= DecisionTreeClassifier(criterion='entropy',random_state=0)
dtc.fit(x_train,y_train)
# y_pred2=dtc.predict(x_test)
# from sklearn.metrics import accuracy_score
# p=accuracy_score(y_test,y_pred2)
# print(p)

from flask import Flask, render_template, url_for, request
import numpy as np
from statistics import mode
app = Flask(__name__, static_folder='./static/')


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/eval', methods=['POST', 'GET'])
def runModel():
    print(request.get_json())
    return 'true'


if __name__ == "__main__":
    app.run(debug=True)