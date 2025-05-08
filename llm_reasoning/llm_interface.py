# llm_reasoning/llm_interface.py
import subprocess

def get_prediction_reasoning(prediction_input):
    """
    Interact with the LLM to get reasoning behind the IPL prediction.
    
    Args:
        prediction_input (str): The input that the model uses for prediction.
    
    Returns:
        str: The reasoning behind the prediction.
    """
    try:
        # Craft the prompt for reasoning based on the prediction input
        prompt = f"Given the match data: {prediction_input}, explain why the predicted team is likely to win."

        # Run the Ollama command to get the reasoning
        result = subprocess.run(
            ["ollama", "run", "llama3", prompt], capture_output=True, text=True
        )

        # If there is an error with the subprocess call, return it
        if result.returncode != 0:
            return f"Error: {result.stderr.strip()}"

        # Return the reasoning (output from the LLM)
        return result.stdout.strip()

    except Exception as e:
        return f"Error while fetching reasoning: {str(e)}"
