import requests

def explain_prediction(input_data):
    team1 = input_data.get("team1", "Team 1")
    team2 = input_data.get("team2", "Team 2")
    toss_winner = input_data.get("toss_winner", "Unknown")
    toss_decision = input_data.get("toss_decision", "Unknown")
    venue = input_data.get("venue", "Unknown Venue")

    prompt = (
        f"Explain in 3 short sentences why {team1} might win against {team2} at {venue}, "
        f"considering {toss_winner} won the toss and chose to {toss_decision}."
    )

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": prompt,
                "stream": False,
                "options": {
                    "num_predict": 100  # LIMIT response size
                }
            },
            timeout=60  # 60 seconds
        )
        result = response.json()
        return result.get("response", "").strip()
    except Exception as e:
        print(f"LLM error: {e}")
        return "LLM explanation not available due to an internal error."
