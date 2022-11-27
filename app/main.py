import pandas as pd

from fastapi import FastAPI
from models import Input, Output
from predlib import get_model_response


app = FastAPI()

model_name = "Iris Setosa"
version = "v1.0.0"


@app.get('/')
async def model_info():
    """Return model information, version, how to call"""
    return {
        "name": model_name,
        "version": version
    }


@app.get('/health')
async def service_health():
    """Return service health"""
    return {
        "ok"
    }


@app.post('/predict', response_model=Output)
async def model_predict(input: Input):
    """Prediction"""
    X = pd.json_normalize(input.__dict__)
    X = X.to_numpy()
    X = X.tolist()
    response = get_model_response(X)
    return response
