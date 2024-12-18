import nltk
from nltk.corpus import words
from greedy import greedy_solver
from heuristic import heuristic_solver

# Get all 5-letter words
nltk.download('words', quiet=True)
dictionary = [word.lower() for word in words.words() if len(word) == 5 and word.isalpha()]


target_words = ["apple", "bread", "chair", "dance", "eagle", "flame", "grass", "house", "jelly", "knife"]

for word in target_words:
    print('Running Greedy Solver')
    greedy_solver(dictionary, word)
    print('Running Heuristic Solver')
    heuristic_solver(dictionary, word)
    break
