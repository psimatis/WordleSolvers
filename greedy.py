from client import get_server_feedback

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