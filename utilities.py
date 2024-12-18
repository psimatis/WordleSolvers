import requests
from typing import Dict, Any

BASE_URL = "https://wordle.votee.dev:8000"

# Calls the given API and play the game
def get_server_feedback(word: str, guess: str) -> Dict[str, Any]:
    """Call the /word/{word} endpoint with a GET request."""
    url = f"{BASE_URL}/word/{word}"
    params = {"guess": guess}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": response.text, "status_code": response.status_code}
    
# Filters candidates depending on the API response
def filter_candidates(candidates, feedback):
    filtered = []
    for word in candidates:
        valid = True
        for fb in feedback:
            slot, char, result = fb["slot"], fb["guess"], fb["result"]
            if result == "correct" and word[slot] != char:
                valid = False
                break
            if result == "present" and (char not in word or word[slot] == char):
                valid = False
                break
            if result == "absent" and char in word:
                valid = False
                break
        if valid:
            filtered.append(word)
    return filtered

# Example Usage
if __name__ == "__main__":
    # Word Guess (GET)
    print("\n--- Word Guess Response ---")
    word_guess_result = get_server_feedback(word="mango", guess="apple")
    print(word_guess_result)
