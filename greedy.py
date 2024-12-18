from utilities import get_server_feedback, filter_candidates

def greedy_solver(dictionary, target):
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

        if not candidates:
            break # method failed to solve wordle
        guess = candidates[0]

    return None, attempts
