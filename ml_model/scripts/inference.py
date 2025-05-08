import os
import joblib
import pandas as pd

# Paths
BASE_DIR = os.path.dirname(os.path.dirname(__file__))  # points to 'ml_model/'
MODEL_PATH = os.path.join(BASE_DIR, "models", "final_pipeline.pkl")

# Load the full pipeline (preprocessing + model)
pipeline = joblib.load(MODEL_PATH)

def predict_winner(match_data: pd.DataFrame):
    # Ensure match_data is a single-row DataFrame with raw inputs (team1, team2, venue, etc.)
    if match_data.shape[0] != 1:
        raise ValueError("match_data must be a single-row DataFrame.")
    
    # Check if match_data contains all required columns
    expected_columns = pipeline.named_steps['preprocessor'].get_feature_names_out()
    
    # Ensure all expected columns are present, and add missing ones (with 0 values)
    for col in expected_columns:
        if col not in match_data.columns:
            match_data[col] = 0  # Add missing columns with 0 values (or appropriate value)

    # The columns should now match the expected columns
    match_data = match_data[expected_columns]  # Reorder columns to match the model's expected order

    # Predict the winner using the pipeline
    prediction = pipeline.predict(match_data)
    
    # Return the prediction
    return prediction[0]
