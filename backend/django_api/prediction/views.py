import sys
import os
import json
import joblib
import pandas as pd
from django.http import JsonResponse
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response

os.environ["OLLAMA_MODELS"] = "D:\\ollama"
 # use your actual new path

# Add the root directory to sys.path to import llm_reasoning module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

from llm_reasoning.llm_explainer import explain_prediction  # Correct import for LLM

# Load model pipeline
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
MODEL_PATH = os.path.join(BASE_DIR, 'ml_model', 'models', 'final_pipeline.pkl')
pipeline = joblib.load(MODEL_PATH)

class PredictWinnerView(APIView):
    def post(self, request, format=None):
        try:
            data = json.loads(request.body)
            df = pd.DataFrame([data])
            prediction = pipeline.predict(df)[0]

            # Get LLM explanation
            explanation = explain_prediction(data)

            return Response({
                "predicted_winner": prediction,
                "reasoning": explanation
            })
        except Exception as e:
            return Response({"error": f"Prediction failed: {str(e)}"}, status=400)

class PredictWithReasoningView(APIView):
    def post(self, request, format=None):
        try:
            data = json.loads(request.body)
            df = pd.DataFrame([data])
            prediction = pipeline.predict(df)[0]

            # Generate explanation using LLM
            explanation = explain_prediction(data)

            return Response({
                "predicted_winner": prediction,
                "reasoning": explanation  # ✅ this matches frontend
            })
        except Exception as e:
            return Response({"error": f"Prediction with reasoning failed: {str(e)}"}, status=400)

class IndexView(View):
    def get(self, request):
        return JsonResponse({"message": "Welcome to the IPL Prediction API! Use the /predict endpoint for predictions."})
