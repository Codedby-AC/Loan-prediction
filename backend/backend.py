from fastapi import FastAPI
from pydantic import BaseModel
import torch
import os
import joblib

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# -----------------------------
# Get Absolute Model Path (SAFE WAY)
# -----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.abspath(
    os.path.join(BASE_DIR, "..", "model", "loan_model.pkl")
)



BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Go one level up (loan_prediction folder)
ROOT_DIR = os.path.abspath(os.path.join(BASE_DIR, ".."))

# Scaler path
scaler_path = os.path.join(ROOT_DIR, "modelscaler.pkl")

scaler = joblib.load(scaler_path)

print("Scaler path:", scaler_path)

# -----------------------------
# Model Architecture (MUST match training)
# -----------------------------
class LoanNN(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(5, 1)

    def forward(self, x):
        return torch.sigmoid(self.linear(x))


# -----------------------------
# Load Model
# -----------------------------
model = LoanNN()

state_dict = torch.load(model_path, map_location="cpu")
model.load_state_dict(state_dict)

model.eval()

print("Model type:", type(model))  # Should print LoanNN


# -----------------------------
# Input Schema
# -----------------------------
class LoanData(BaseModel):
    no_of_dependents: int
    education: int
    self_employed: int
    loan_term: int
    cibil_score: int


# -----------------------------
# Prediction Route
# -----------------------------

import numpy as np

@app.post("/predict")
def predict(data: LoanData):

    # 1️⃣ First make numpy array (NOT tensor)
    input_array = np.array([[
        data.no_of_dependents,
        data.education,
        data.self_employed,
        data.loan_term,
        data.cibil_score
    ]])

    # 2️⃣ Apply scaler
    input_scaled = scaler.transform(input_array)

    # 3️⃣ Convert scaled data to tensor
    input_tensor = torch.tensor(input_scaled, dtype=torch.float32)

    # 4️⃣ Prediction
    with torch.no_grad():
        output = model(input_tensor)
        probability = output.item()
        prediction = 1 if probability > 0.5 else 0

    return {
        "prediction": prediction,
        "probability": round(probability, 4)
    }


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
def home():
    return {"message": "Loan prediction api is running 🚀"}

