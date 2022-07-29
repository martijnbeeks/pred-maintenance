import os
import uvicorn
from fastapi import FastAPI, Request
from joblib import dump, load
import pandas as pd
import config
import json
from utils import RecordedDate

from typing import TypeVar

PandasDataFrame = TypeVar('pandas.core.frame.DataFrame')

app = FastAPI()

clf = load(config.PATH_MODEL)

@app.get("/")
def read_root():
    return {"message": "Welcome from the API"}


@app.post("/predict")
def predict(data: dict):
    df = pd.DataFrame([data])
    predictions = clf.predict_proba(df)
    return {'prediction': json.dumps(predictions.tolist())}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080)