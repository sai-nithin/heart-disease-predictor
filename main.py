import numpy as np 
from flask import Flask,render_template,request
import pickle
app=Flask(__name__)
model=pickle.load(open('model.pkl', 'rb'))
@app.route("/")
def home():
	return render_template("home.html")
@app.route("/pro")
def pro():
	return render_template("pro.html",values=None)
@app.route("/predict",methods=['POST'])
def predict():
	age=request.form.get('age')
	sex=request.form.get('sex')
	cp=request.form.get('cp')
	trestbps=request.form.get('trestbps')
	chol=request.form.get('chol')
	fbs=request.form.get('fbs')
	restecg=request.form.get('restecg')
	thalach=request.form.get('thalach')
	exang=request.form.get('exang')
	oldpeak=request.form.get('oldpeak')
	slope=request.form.get('slope')
	ca=request.form.get('ca')
	thal=request.form.get('thal')
	li=[int(age),int(sex),int(cp),int(trestbps),int(chol),int(fbs),int(restecg),
	    int(thalach),int(exang),oldpeak,int(slope),int(ca),int(thal)]
	final=[np.array(li)]
	prediction=model.predict(final)
	output=round(prediction[0])
	print(output)
	return render_template("pro.html",values=output)
if __name__ =="__main__":
	app.run(debug=True)
