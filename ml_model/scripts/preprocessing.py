import joblib

def load_preprocessor():
    # Load the preprocessor from a saved file (replace with your actual path)
    preprocessor = joblib.load('ml_model/models/preprocessor.pkl')  # Adjust the path as needed
    return preprocessor
