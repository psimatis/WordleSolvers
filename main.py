from client import get_server_feedback


target_words = ["apple", "bread", "chair", "dance", "eagle", "flame", "grass", "house", "jelly", "knife"]

for word in target_words:
    guess = "apple"
    print(get_server_feedback(word, guess))
