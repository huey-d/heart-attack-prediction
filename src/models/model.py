import time
import os

import pandas as pd
import numpy as np


import sklearn
import sklearn.model_selection
import sklearn.preprocessing
import sklearn.metrics

import pickle
import hyperopt
from hyperopt.pyll import scope
import xgboost
import mlflow


param_space = {'eta': hyperopt.hp.loguniform('eta', -9, 0),
              'gamma': hyperopt.hp.loguniform('gamma', -10, 10),
              'max_depth': scope.int(hyperopt.hp.uniform('max_depth', 1, 30)),
              'min_child_weight': hyperopt.hp.loguniform('min_child_weight', -2, 3),
              'max_delta_step': hyperopt.hp.uniform('max_delta_step', 1, 10),
              'subsample': hyperopt.hp.uniform('subsample', 0.5, 1),
              'colsample_bytree': hyperopt.hp.uniform('colsample_bytree', 0.5, 1),
              'lambda': hyperopt.hp.loguniform('lambda', -10, 10),
              'alpha': hyperopt.hp.loguniform('alpha', -10, 10),
              'scale_pos_weight': hyperopt.hp.uniform('scale_pos_weight', 1, 10),
              'grow_policy': hyperopt.hp.choice('grow_policy', ['depthwise', 'lossguide']),
              'max_leaves': scope.int(hyperopt.hp.uniform('max_leaves', 0, 10)),
              'n_estimators': scope.int(hyperopt.hp.uniform('n_estimators', 100, 1000)),
              'eval_metric': hyperopt.hp.choice('eval_metric', ['logloss', 'error'])
              }


def read_data(data_path: str = "data", file_path: str = "raw/heart.csv"):
    df = pd.read_csv(os.path.join(data_path, file_path))
    
    X = df.drop(columns=['output'], axis=1).values
    y = df['output'].values

    return X, y


def classify(X: np.ndarray,
             y: np.ndarray,
             approach: str='bayes',
             scale: str = True):

    start = time.time()
    
    X_train, X_test, y_train, y_test  = sklearn.model_selection.train_test_split(X, y, test_size=0.2, random_state=42)

    # Normalize data
    if scale:
        scaler = sklearn.preprocessing.MinMaxScaler()
        X_train = scaler.fit_transform(X_train)

    eval_set = [(X_train, y_train), (X_test, y_test)]
    
    def train_model(params):

        mlflow.xgboost.autolog(silent=True)

        with mlflow.start_run(nested=True):
            

            start_time = time.time()
            model = xgboost.XGBClassifier(**params, objective='binary:logistic', early_stopping_rounds=200, n_jobs=-1)
            model.fit(X_train, y_train, verbose=True, eval_set=eval_set)
            run_time = time.time() - start_time
            

            # Make predictions for the classifier
            y_pred = model.predict(X_test)


            # use sklearn.metrics to log metrics onto mlflow
            b_acc = sklearn.metrics.balanced_accuracy_score(y_test, y_pred)
            precision = sklearn.metrics.precision_score(y_test, y_pred, average='macro')
            f1 = sklearn.metrics.f1_score(y_test, y_pred, average='macro')

            cm = sklearn.metrics.confusion_matrix(y_test, y_pred)
            mat_display = sklearn.metrics.ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=['Not at Risk', 'At Risk'])

            precision_graph, recall_graph, _ = sklearn.metrics.precision_recall_curve(y_test, y_pred)
            pr_display = sklearn.metrics.PrecisionRecallDisplay(precision=precision_graph, recall=recall_graph)


            mlflow.log_metric('balanced_acc', b_acc)
            mlflow.log_metric('precision', precision)
            mlflow.log_metric('f1', f1)
            mlflow.log_metric('run_time', run_time)

            
            return {'status': hyperopt.STATUS_OK, 'loss': -f1, 'model': model}

    trials = hyperopt.Trials()
    best_params = hyperopt.fmin(fn=train_model,
                                space=param_space,
                                algo=hyperopt.tpe.suggest,
                                max_evals=25,
                                trials=trials
                                )


    model_runtime = time.time() - start
    
    best_trial = -1 * trials.average_best_error()
    best_parameters = hyperopt.space_eval(param_space, best_params)

    print("\nBest Hyperparameters: {}".format(best_parameters))
    print("\nBest F1 Score: {}".format(best_trial * 100))
    print("\nModel runtime: {} seconds".format(model_runtime))

    best_model = trials.results[np.argmin([r['loss'] for r in trials.results])]['model']
    print(best_model)
    
    final_model_path = "models/"
    backend_model_path = "backend/"
    pickle.dump(best_model, open(final_model_path+'xgboost.pkl', 'wb'))
    pickle.dump(best_model, open(backend_model_path+'xgboost.pkl', 'wb'))



if __name__== '__main__':
    X, y = read_data()
    classify(X, y)