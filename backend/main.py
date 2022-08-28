import json
import pickle
from fastapi import Body, FastAPI
from pydantic import BaseModel
import uvicorn
import xgboost
import requests

app = FastAPI(title="Heart Attack API", description="API for Heart Attack Classification")

# Creating class for inputs to the model.
class HeartAttack(BaseModel):
    age : int
    sex : int
    cp : int
    trtbps : int
    chol : int
    fbs : int
    restecg : int
    thalachh : int
    exng : int
    oldpeak : float
    slp : int
    caa : int
    thall : int

# homepage route
@app.get("/")
def read_root():
	return {'message': 'This is the homepage of the API '}

# Loading trained model
with open('./deploy_xgboost.pkl', "rb") as f:
    loaded_model = pickle.load(f)

# Sending a post request to the “/prediction” route with a request body.
# The request body contains the key-value pairs of the parameters
# We should expect a JSON response with heart attack risk classified.

# Columns are: ['age', 'sex', 'cp', 'trtbps', 'chol', 'fbs', 'restecg', 'thalachh', 'exng', 'oldpeak', 'slp', 'caa', 'thall']
@app.post('/predict')
async def get_risk(data: HeartAttack):
    received = data.dict()
    age = received['age']
    sex = received['sex']
    cp = received['cp']
    trtbps = received['trtbps']
    chol = received['chol']
    fbs = received['fbs']
    restecg = received['restecg']
    thalachh = received['thalachh']
    exng = received['exng']
    oldpeak = received['oldpeak']
    slp = received['slp']
    caa = received['caa']
    thall = received['thall']
    
    features = [[age, sex, cp, trtbps, chol, fbs, restecg, thalachh, exng, oldpeak, slp, caa, thall]]
    pred_name = loaded_model.predict(features).tolist()[0]
    if pred_name == 1:
        pred_name = 'Higher Risk of Heart Attack'
    else:
        pred_name = 'Lower Risk of Heart Attack'
    
    return pred_name