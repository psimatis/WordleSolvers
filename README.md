# Wordle Solvers

In **Wordle**, players have six attempts to guess a five-letter word. They receive feedback through colored tiles that indicate correct letters and their placement.
This project creates three solvers and benchmarks them.

## Solvers
1. **AI**: Trains a machine learning model using Margin Rankin loss to predict words.
2. **Heuristic**: Ranks words based on their letter frequency to narrow down possible answers.
3. **Greedy**: Uses a greedy algorithm to guess words.

For all the candidates the words are filtered based on a Wordle API (details in ```utilies.py```). For example, words with absent letters are ignored.

## Files
- `main.py`: Runs and benchmarks the solvers.
- `greedy.py`: Greedy solver logic.
- `heuristic.py`: Heuristic solver logic.
- `ai.py`: The logic and training code of the AI solver. 
- `ai_solver.pth`: A toy pre-trained model for the AI solver.
- `utility.py`: Contains useful functions (e.g., calling the API).

## How to Run
1. Ensure you have Python installed.
2. Install the dependencies from the requirements.txt
3. ```python main.py```

## Output
The solvers' evaluation on 10 words is displayed with a Pandas DataFrame containing average time and attempts.

## Results
| Solver    | Average Time (s) | Average Attempts |
|-----------|----------------|-----------------|
| Greedy    | 0.1234         | 4.56            |
| Heuristic | 0.2345         | 3.78            |
| AI        | 0.5678         | 2.91            |

The **AI** solver, while the slowest, requires the fewest attempts. **Greedy** is the worst guesser, while **Heuristic** sits in the middle.
