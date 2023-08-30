import json
import requests

if __name__ == '__main__':
    ftrs = {
        'age': 54,
        'sex': 1,
        'cp': 0,
        'trestbps': 122,
        'chol': 286,
        'fbs':  0,
        'restecg': 0,
        'thalach': 116,
        'exang': 1,
        'oldpeak': 1.6,
        'slope': 1,
        'ca': 0,
        'thal':2
    }
    url = 'https://flknyjlpf5.execute-api.eu-west-2.amazonaws.com/dev/api' #'http://127.0.0.1:5000/api'
    r = requests.post(url,json=ftrs)
    print(r.json())