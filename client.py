import requests
from typing import Dict, Any

# Base URL
BASE_URL = "https://wordle.votee.dev:8000"


def get_server_feedback(word: str, guess: str) -> Dict[str, Any]:
    """Call the /word/{word} endpoint with a GET request."""
    url = f"{BASE_URL}/word/{word}"
    params = {"guess": guess}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": response.text, "status_code": response.status_code}

# Example Usage
if __name__ == "__main__":
    # Word Guess (GET)
    print("\n--- Word Guess Response ---")
    word_guess_result = get_server_feedback(word="mango", guess="apple")
    print(word_guess_result)
