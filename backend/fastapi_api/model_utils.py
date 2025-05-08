# backend/fastapi_api/model_utils.py

import os
import joblib
import pandas as pd

# Paths
BASE_DIR = os.path.dirname(os.path.dirname(__file__))  # goes up from fastapi_api/
MODEL_PATH = os.path.join(BASE_DIR, '..', 'ml_model', 'models', 'match_winner_model.pkl')


print(f"🔍 Looking for model at: {MODEL_PATH}")  # Add this line to debug
X_SAMPLE_PATH = os.path.join(BASE_DIR, '..', 'ml_model', 'data', 'X.csv')
print("📄 Loading sample X data from:", X_SAMPLE_PATH)


# Load model
model = joblib.load(MODEL_PATH)
X_sample = pd.read_csv(X_SAMPLE_PATH)  # To get column structure

def predict_winner(input_dict: dict) -> str:
    input_df = pd.DataFrame([input_dict])
    input_df = pd.get_dummies(input_df)

    # Align input columns with training data
    input_df = input_df.reindex(columns=X_sample.columns, fill_value=0)

    prediction = model.predict(input_df)[0]
    return prediction
