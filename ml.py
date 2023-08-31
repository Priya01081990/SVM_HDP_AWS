import os
from sklearn import svm
import pandas as pd
import pickle

if __name__ == '__main__':

    CAT_FTRS = ["cp", "fbs", "restecg", "exang", "slope", "ca", "thal",]
    NUM_FTRS = ["age","trestbps", "chol", "thalach", "oldpeak"]
    SCALE = {
    'age': 54.43414634146342,
    'trestbps':131.61170731707318,
    'chol':246.0,
    'thalach':149.11414634146342,
    'oldpeak':1.0715121951219515,
    }
    C = 0.372759
    GAMMA = 0.051795
    svm_rbf = svm.SVC(
        C=C,
        kernel="rbf",
        gamma=GAMMA,
        shrinking=True,
        probability=True,
        tol=0.001,
        cache_size=200000,
        class_weight='balanced',
    )
    os.system("aws s3 cp s3://publicdatasetsthesis/heart.csv ./data/heart.csv")
    if os.path.exists("./data/heart.csv"):
        df = pd.read_csv("./data/heart.csv")
        for c in df.columns:
            if c in SCALE.keys():
                df[c] =[(x - SCALE[c]) for x in df[c].tolist()]
        target_col_name = "target"
        X = df[[c for c in df.columns if c != target_col_name]].to_numpy()
        Y = df[[target_col_name]].to_numpy()
        svm_rbf.fit(X=X, y=Y)
        pickle.dump(svm_rbf, open("SVM_hdp.pickle", "wb"))

