from collections import Counter
from utilities import get_server_feedback, filter_candidates


# Rank candidates based on letter frequency
def rank_candidates(word_list):
    letter_counter = Counter("".join(word_list))    
    def word_score(word):
        return sum(letter_counter[letter] for letter in set(word))
    
    return sorted(word_list, key=word_score, reverse=True)


def heuristic_solver(dictionary, target):
    candidates = dictionary
    guess = "earth"
    attempts = 0

    while candidates:
        attempts += 1
        feedback = get_server_feedback(target, guess)
        print(f"Attempt {attempts} Guess: {guess} Feedback: {feedback}")

        if all(fb["result"] == "correct" for fb in feedback):
            return guess, attempts
        
        candidates = filter_candidates(candidates, feedback)
        candidates = rank_candidates(candidates)
        if not candidates:
            break # method failed to solve wordle
        guess = candidates[0]

    return None, attempts