# ml_model/scripts/prediction_reasoning.py
from llm_reasoning.llm_interface import get_prediction_reasoning

def get_match_prediction_reasoning(prediction_input):
    """
    Fetch reasoning for the match prediction by calling the LLM interface.
    
    Args:
        prediction_input (str): The prediction input.
    
    Returns:
        str: The reasoning behind the prediction.
    """
    reasoning = get_prediction_reasoning(prediction_input)
    return reasoning
