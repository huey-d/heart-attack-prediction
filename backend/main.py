import json
import pickle

from fastapi import Body, FastAPI
from fastapi.logger import logger
from pydantic import BaseModel
import uvicorn

import xgboost

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


# Loading trained model
with open('./deploy_xgboost.pkl', "rb") as f:
    loaded_model = pickle.load(f)

# Sending a post request to the “/prediction” route with a request body.
# The request body contains the key-value pairs of the parameters
# We should expect a JSON response with heart attack risk classified.

# Columns are: ['age', 'sex', 'cp', 'trtbps', 'chol', 'fbs', 'restecg', 'thalachh', 'exng', 'oldpeak', 'slp', 'caa', 'thall']
@app.post('/prediction')
def get_risk(data: HeartAttack):
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
    pred_name = loaded_model.predict([[age, sex, cp, trtbps, chol, fbs, restecg, thalachh, exng, oldpeak, slp, caa, thall]]).tolist()[0]
    return  {'Prediction' : pred_name}
    

# @app.post('/subscription')
# def subscription(data :dict = Body(...)):
#     #output_data=await data.json()
#     print(data)


# @app.get("/get_entities/{id}")
# async def get_entities(id:str ):
    
#     url="http://orion.docker:1026/ngsi-ld/v1/entities/" +  id + "?options=keyValues"

#     client = httpx.Client()
#     response = client.get(url)
    
#     logger.info(response.json())
#     return response.json()

# @app.patch("/prediction/{id}/{potability}")
# def notify_prediction(id:str,potability:str):
#     url = "http://orion.docker:1026/ngsi-ld/v1/entities/" + id + "/attrs/Potability"

#     payload = json.dumps({
# 	"value": potability,
# 	"type": "Property"
# 	})
#     headers = {
# 	'Content-Type': 'application/json',
# 	'Link': '<http://context/ngsi-context.jsonld>; rel="http://www.w3.org/ns/json-ld#context"; type="application/ld+json"'
# 	}
#     client = httpx.Client()
#     response = client.patch(url, headers=headers, data=payload)

#     return response.json()


# homepage route
@app.get("/")
def read_root():
	return {'message': 'This is the homepage of the API '}
