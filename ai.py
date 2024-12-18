import nltk
import torch
import torch.nn as nn
import torch.optim as optim
from nltk.corpus import words
import random
from utilities import get_server_feedback, filter_candidates

random.seed(0)
torch.manual_seed(0)

nltk.download('words', quiet=True)
dictionary = [word.lower() for word in words.words() if len(word) == 5 and word.isalpha()]
random.shuffle(dictionary)

WORD_LENGTH = 5
ALPHABET = "abcdefghijklmnopqrstuvwxyz"
TRAIN_WORD_COUNT = 5000
PATH = "ai_solver.pth"

class WordleNN(nn.Module):
    def __init__(self, word_length, alphabet_length, hidden_size):
        super(WordleNN, self).__init__()
        self.fc1 = nn.Linear(alphabet_length * word_length, hidden_size)
        self.fc2 = nn.Linear(hidden_size, 1)
    
    def forward(self, x):
        x = torch.relu(self.fc1(x))
        return self.fc2(x)
    
def one_hot_encode(word):
    one_hot = torch.zeros(WORD_LENGTH * len(ALPHABET))
    for i, char in enumerate(word):
        one_hot[i * len(ALPHABET) + ALPHABET.index(char)] = 1
    return one_hot

def train_model(train_words, dictionary, epochs=10):
    model = WordleNN(WORD_LENGTH, len(ALPHABET), 64)
    optimizer = optim.Adam(model.parameters(), lr=0.001)
    criterion = nn.MarginRankingLoss(margin=1.0)

    for epoch in range(epochs):
        total_loss = 0.0
        for target_word in train_words:
            positive_guess = target_word
            negative_guess = random.choice(dictionary)

            if positive_guess == negative_guess:
                continue

            x_positive = one_hot_encode(positive_guess)
            x_negative = one_hot_encode(negative_guess)

            score_positive = model(x_positive).squeeze()
            score_negative = model(x_negative).squeeze()
            target = torch.tensor(1.0) 
            loss = criterion(score_positive, score_negative, target)

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            total_loss += loss.item()
        print(f"Epoch {epoch + 1}, Loss: {total_loss:.4f}")
    torch.save(model.state_dict(), PATH)
    print(f"Model saved to {PATH}")

# Load the model
def load_model(path):
    model = WordleNN(WORD_LENGTH, len(ALPHABET), 64)
    model.load_state_dict(torch.load(path, weights_only=False))
    model.eval()
    print(f"Model loaded from {path}")
    return model

def predict(model, candidates):
    scores = []
    for c in candidates:
        x = one_hot_encode(c)
        with torch.no_grad():
            score = model(x)
        scores.append((c, score.item()))
    scores.sort(key=lambda x: x[1], reverse=True)
    return scores[0][0]


def ai_solver(model, dictionary, target):
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
        guess = predict(model, candidates)

    return None, attempts


if __name__ == "__main__":
    # Split dataset into training and test words
    train_words = dictionary[:TRAIN_WORD_COUNT]
    test_words = dictionary[TRAIN_WORD_COUNT:TRAIN_WORD_COUNT + 100]

    # Train the model
    print("Training the Wordle solver...")
    model = train_model(train_words, dictionary)

    # Load the model
    model = load_model(PATH)

    # Rank words on test set
    print("\nRanking test words...")
    best_word = predict(model, test_words)
    print(f"Best word: {best_word}")

    # Rank custom candidates
    custom_candidates = ["apple", "grape", "peach", "mango", "berry"]
    print("\nRanking custom candidates...")
    for word in custom_candidates:
        x = one_hot_encode(word)
        with torch.no_grad():
            score = model(x.unsqueeze(0)).item()
        print(f"{word}: {score:.4f}")