import nltk
import time
import pandas as pd
from nltk.corpus import words
from greedy import greedy_solver
from heuristic import heuristic_solver
from ai import ai_solver, load_model

# Get all 5-letter words
nltk.download('words', quiet=True)
dictionary = [word.lower() for word in words.words() if len(word) == 5 and word.isalpha()]

target_words = ["apple", "bread", "chair", "dance", "eagle", "flame", "grass", "house", "jelly", "knife"]

# Initialize timers and attempts tracking
greedy_times, greedy_attempts = [], []
heuristic_times, heuristic_attempts = [], []
ai_times, ai_attempts = [], []

# Load AI model once
model = load_model("ai_solver.pth")

for word in target_words:
    print(f"Running solvers for target word: {word}")

    # Greedy Solver
    start_time = time.time()
    greedy_result = greedy_solver(dictionary, word)
    greedy_times.append(time.time() - start_time)
    greedy_attempts.append(greedy_result[1])

    # Heuristic Solver
    start_time = time.time()
    heuristic_result = heuristic_solver(dictionary, word) 
    heuristic_times.append(time.time() - start_time)
    heuristic_attempts.append(heuristic_result[1])

    # # AI Solver
    start_time = time.time()
    ai_result = ai_solver(model, dictionary, word)  # Should return (word, attempts)
    ai_times.append(time.time() - start_time)
    ai_attempts.append(ai_result[1])

# Create a DataFrame to display results
results_df = pd.DataFrame({
    "Solver": ["Greedy", "Heuristic", "AI"],
    "Average Time (s)": [
        sum(greedy_times) / len(greedy_times),
        sum(heuristic_times) / len(heuristic_times),
        sum(ai_times) / len(ai_times)
    ],
    "Average Attempts": [
        sum(greedy_attempts) / len(greedy_attempts),
        sum(heuristic_attempts) / len(heuristic_attempts),
        sum(ai_attempts) / len(ai_attempts)
    ]
})

# Print the DataFrame
print("\nSolver Performance Summary:")
print(results_df)

