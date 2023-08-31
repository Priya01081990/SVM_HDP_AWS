# Deploy ML Model (sklearn svm) to AWS Lambda

This project is about how to upload an ml model to aws lambda.

It assumes that user has 
 - AWSCLI installed
 - user runs 'aws configure' to set proper parameters for aws connection
 - user has python 3.9
 - user has 'virtual env'

# Steps

Following are the steps to deploy the saved ML model as an AWS Lambda API

    - Download the project from git
    - cd 'project_dir'
    - Activate 'venv' and install from 'install.txt'
    - run `python ml.py` to create the model (SVM_hdp.pickle) in the current project directory
    - run 'zappa deploy7update '__Project__NAME__' (e.g. dev)


# How to interact with the API

Following is a python code snippet that shows how to call the api
```python
    import json
    import requests
    
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
    url = 'API_URL' # or localhost 'http://127.0.0.1:5000/api'
    r = requests.post(url,json=ftrs)
    print(r.json())
```
The output should look like following

```
{ 
    'prediction':1, 
    'description':'probability of heat disease: 1 = Present, 0 = Absent', 
    'confidence':90.91
}
```

