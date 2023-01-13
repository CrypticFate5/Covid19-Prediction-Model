from flask import Flask,render_template,request
import numpy as np
import pickle

model=pickle.load(open('model_final.pkl','rb'))

app=Flask(__name__)


@app.route('/predict' , methods=["POST"])
def predict():
    a=(int)(request.form['usmr'])
    b=(int)(request.form['patient_type'])
    c=(int)(request.form['pneumonia'])
    d=(int)(request.form['age'])
    e=(int)(request.form['diabetes'])
    f=(int)(request.form['hypertension'])
    g=(int)(request.form['renal_chronic'])
    input=[a,b,c,d,e,f,g,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    h=(int)(request.form['medical_unit'])
    input[5+h]=1
    i=(int)(request.form['classification'])
    input[17+i]=1
    input=np.array(input)
    input=input.reshape(1,25)
    print(input)
    prediction=model.predict(input)
    print(prediction)
    if(prediction[0]==1):
        ans="The patient has low chances of survival"
    else:
        ans="The patient has high chances of survival"

    return render_template('resultspage.html' , answer=ans)
 
@app.route('/')
def main():
    return render_template('index.html')
app.run(debug=True)