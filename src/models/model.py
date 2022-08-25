import time
import os

import pandas as pd
import numpy as np


import sklearn
import sklearn.model_selection
import sklearn.preprocessing
import sklearn.metrics

import pickle
import xgboost
import mlflow


def read_data(data_path: str = "data", file_path: str = "raw/heart.csv"):
    df = pd.read_csv(os.path.join(data_path, file_path))
    
    X = df.drop(columns=['output'], axis=1).values
    y = df['output'].values

    return X, y


def classify(X: np.ndarray,
             y: np.ndarray,
             scale: str = True):

    start = time.time()
    
    X_train, X_test, y_train, y_test  = sklearn.model_selection.train_test_split(X, y, test_size=0.2, random_state=42)

    # Normalize data
    if scale:
        scaler = sklearn.preprocessing.MinMaxScaler()
        X_train = scaler.fit_transform(X_train)

    eval_set = [(X_train, y_train), (X_test, y_test)]
    

    mlflow.xgboost.autolog(silent=True)

    with mlflow.start_run(nested=True):
        start_time = time.time()
        model = xgboost.XGBClassifier(objective='binary:logistic', early_stopping_rounds=100, n_jobs=-1)
        model.fit(X_train, y_train, verbose=True, eval_set=eval_set)
        run_time = time.time() - start_time

        # Make predictions for the classifier
        y_pred = model.predict(X_test)

        # use sklearn.metrics to log metrics onto mlflow
        b_acc = sklearn.metrics.balanced_accuracy_score(y_test, y_pred)
        precision = sklearn.metrics.precision_score(y_test, y_pred, average='macro')
        f1 = sklearn.metrics.f1_score(y_test, y_pred, average='macro')

        mlflow.log_metric('balanced_acc', b_acc)
        mlflow.log_metric('precision', precision)
        mlflow.log_metric('f1', f1)
        mlflow.log_metric('run_time', run_time)

    model_runtime = time.time() - start
    print("\nModel runtime: {} seconds".format(model_runtime))
    
    final_model_path = "models/"
    pickle.dump(model, open(final_model_path+'xgboost.pkl', 'wb'))



if __name__== '__main__':
    X, y = read_data()
    classify(X, y)