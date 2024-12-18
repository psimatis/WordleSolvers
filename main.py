import nltk
from nltk.corpus import words
from client import get_server_feedback
from greedy import greedy_solver

# Get all 5-letter words
nltk.download('words', quiet=True)
dictionary = [word.lower() for word in words.words() if len(word) == 5 and word.isalpha()]


target_words = ["apple", "bread", "chair", "dance", "eagle", "flame", "grass", "house", "jelly", "knife"]

for word in target_words:
    greedy_solver(dictionary, word)
    break
