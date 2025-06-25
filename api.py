from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
import mlflow.pyfunc

app = FastAPI()

# Load the model from MLflow (adapt the path to your setup)
try:
    model = mlflow.pyfunc.load_model("model")  # or "mlruns/0/<run_id>/artifacts/model"
except Exception as e:
    model = None
    print(f"Warning: model not loaded - {e}")

# Define input schema (adapt fields to your dataset)
class InputData(BaseModel):
    feature1: float
    feature2: float
    feature3: float

@app.get("/")
def read_root():
    return {"message": "API is running"}

@app.post("/predict")
def predict(data: InputData):
    if model is None:
        raise HTTPException(status_code=503, detail="Model not available")

    try:
        df = pd.DataFrame([data.dict()])
        prediction = model.predict(df)
        return {"prediction": prediction.tolist()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction failed: {e}")

## test