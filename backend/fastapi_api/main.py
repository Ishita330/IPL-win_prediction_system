from fastapi import FastAPI
from llm_reasoning.llm_explainer import explain_prediction
from pydantic import BaseModel
import pandas as pd
import joblib
import os
from ml_model.scripts.prediction_reasoning import get_match_prediction_reasoning  # Importing reasoning function

# Load the trained model and preprocessing pipeline
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, 'ml_model', 'models', 'final_pipeline.pkl')
pipeline = joblib.load(MODEL_PATH)

app = FastAPI()

# Define input schema for match data
class MatchInput(BaseModel):
    team1: str
    team2: str
    toss_winner: str
    toss_decision: str
    venue: str
    batting_team: str
    bowling_team: str
    runs: int
    wickets: int
    overs: float
    target: int

@app.get("/")
def root():
    return {"message": "🏏 IPL Match Winner Prediction API"}

@app.post("/predict")
def predict(match: MatchInput):
    match_df = pd.DataFrame([match.dict()])
    
    try:
        prediction = pipeline.predict(match_df)
        explanation = explain_prediction(match.dict())
    except Exception as e:
        return {"error": f"Prediction failed: {str(e)}"}

    return {
        "predicted_winner": prediction[0],
        "reasoning": explanation
    }


@app.post("/predict_reasoning")
def predict_reasoning(match: MatchInput):
    """
    Get the reasoning behind the match prediction.
    """
    # Convert match data to a string format for LLM input
    prediction_input = f"Match between {match.team1} and {match.team2}, toss winner: {match.toss_winner}, toss decision: {match.toss_decision}, venue: {match.venue}"
    
    try:
        # Get reasoning for the prediction from the LLM
        reasoning = get_match_prediction_reasoning(prediction_input)
    except Exception as e:
        return {"error": f"Reasoning failed: {str(e)}"}

    return {"reasoning": reasoning}
