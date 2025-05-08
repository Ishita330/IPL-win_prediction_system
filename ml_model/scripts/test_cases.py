# test_cases.py
from inference import predict_winner

def test_case_1():
    input_data = {
        "batting_team": "Mumbai Indians",
        "bowling_team": "Chennai Super Kings",
        "venue": "Wankhede Stadium",
        "runs": 145,
        "wickets": 3,
        "overs": 16.2,
        "target": 175
    }
    result = predict_winner(input_data)
    print("Prediction:", result)

if __name__ == "__main__":
    test_case_1()
