# Wordle Solvers

This project creates and benchmarks three solvers (i.e., Greedy, Heuristic, and AI) using a dictionary of 5-letter words.

## Solvers
1. **Greedy Solver**: Uses a basic greedy algorithm to guess words.
2. **Heuristic Solver**: Ranks candidate words based on their letter frequency to narrow down possible answers.
3. **AI Solver**: Trains a machine learning model using Margin Rankin loss to predict words.

For all the candidates the words are filtered based on the API response. For example, words with absent letters are ignored.

## Files
- `main.py`: Runs and benchmark the solvers.
- `greedy.py`: The logic of the greedy solver.
- `heuristic.py`: The logic of the heuristic solver.
- `ai.py`: The logic and training of the AI solver. 
- `ai_solver.pth`: A toy pre-trained model for the AI solver.
- `utility.py`: Contains useful functions (e.g., calling the API).

## How to Run
1. Ensure you have Python installed.
2. Install the dependencies from the requirements.txt
3. python main.py

## Output
The solver evaluation on 10 words is displayed with a Pandas DataFrame containing average time and attempts.

## Example Output
```plaintext
Solver Performance Summary:
      Solver  Average Time (s)  Average Attempts
0     Greedy            0.1234             4.56
1  Heuristic            0.2345             3.78
2         AI            0.5678             2.91
Results saved to solver_performance_summary.csv

## Who am i?
Panos Simatis
psimatis@hotmail.com
+852 59357074
```

