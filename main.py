# Import libraries
import numpy as np
from flask import Flask, request, jsonify
import pickle


app = Flask(__name__)
# Load the model


MODEL = pickle.load(open("SVM_hdp.pickle", "rb"))
FTRS = "age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal".split(",")
SCALE = {
    'age': 54.43414634146342,
    'trestbps':131.61170731707318,
    'chol':246.0,
    'thalach':149.11414634146342,
    'oldpeak':1.0715121951219515,
    }

@app.route('/api',methods=['POST'])
def predict():
    # Get the data from the POST request.
    data = request.get_json(force=True)
    vals = []
    for c in FTRS:
        if c in SCALE:
            vals.append(float(data.get(c)) - SCALE.get(c))
        else:
            vals.append(float(data.get(c)))
    vals = np.array([vals])
    y = MODEL.predict(vals)[0].tolist()
    conf = float(MODEL.predict_proba(vals)[0].tolist()[0]*100)
    conf = round(conf,2)
    return { 'prediction':y , 'description':'probability of heat disease: 1 = Present, 0 = Absent', 'confidence':conf}


if __name__ == '__main__':
    app.run(port=5001, debug=True)