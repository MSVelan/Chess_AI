# Chess AI with Pygame

This project is a chess game implemented in Python using Pygame for the graphical user interface (GUI) and includes a basic AI opponent (depth can be adjusted). The AI uses a decision-making algorithm for move prediction, running in a separate process from the user interface to keep the UI responsive during gameplay.

![Screenshot](https://github.com/MSVelan/Chess_AI/blob/main/assets/Game_screenshot.png)

## Table of Contents

- [Chess AI with Pygame](#chess-ai-with-pygame)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Technologies](#technologies)
  - [Project Structure](#project-structure)
  - [How to run](#how-to-run)
    - [Development](#development)
    - [Creating the binary/executable:](#creating-the-binaryexecutable)
    - [Installing as a library](#installing-as-a-library)
  - [How the AI works](#how-the-ai-works)
  - [How the AI Finds the Best Move](#how-the-ai-finds-the-best-move)
    - [1. Simple Greedy Method](#1-simple-greedy-method)
    - [2. Minimax Algorithm](#2-minimax-algorithm)
    - [3. NegaMax Algorithm](#3-negamax-algorithm)
    - [4. NegaMax Algorithm with Alpha-Beta Pruning](#4-negamax-algorithm-with-alpha-beta-pruning)
    - [Summary of Algorithms](#summary-of-algorithms)
  - [Future improvement](#future-improvement)
  - [Project Recording](#project-recording)

## Features
- **Multiprocessing**: The UI is implemented as a separate process where 
- **Play against AI**: Users can play a game of chess against an AI opponent.
- **AI vs AI**: We can set both the players to be AI
- **AI Algorithm**: The AI is implemented using a basic algorithm for predicting moves, Nega Max alpha beta pruning is being used.  
- **Responsive UI**: The user interface runs in a separate process, ensuring smooth gameplay without freezing during AI decision-making.
- **Chess Rules**: The game enforces standard chess rules, including legal moves and special moves like castling and en passant, undo move, check for pins and checks, animated moves, move log, high squares
- **Game State Management**: The current state of the game is maintained, allowing for features like undoing moves.

## Technologies

- **Language**: Python
- **Library**: Pygame for the graphical user interface
- **Multiprocessing**: Python's `multiprocessing` module to separate the UI and AI logic processes

## Project Structure

- **assets**: Directory containing sample recording and screenshot of the game 
- **Chess/images**: Directory containing all images of chess pieces
- **Chess/ChessEngine.py**: Implemented the chess game by maintaining the game state, implements various features such as undo move, en passant, etc.
- **Chess/SmartMoveFinder.py**: Implemented the logic for predicting moves, tried various algorithms such as greedy, min-max, nega max, nega max with alpha beta pruning
- **Chess/ChessMain.py**: Integrated the ChessEngine.py and SmartMoveFinder.py files and created the UI using pygame, multiprocessing.

## How to run

### Development

- Clone the github repository
```bash
git clone git@github.com:MSVelan/Chess_AI.git
```

- Ensure dependencies are installed
```bash
pipenv shell
```

### Creating the binary/executable:

```bash
git clone git@github.com:MSVelan/Chess_AI.git
```

```bash
pip install pyinstaller
pyinstaller --onefile --add-data "Chess/images:Chess/images" --name ChessMain Chess/ChessMain.py
./dist/ChessMain
```
### Installing as a library

Download dist/chess_bot-1.0-py3-none-any.whl or dist/chess_bot-1.0.tar.gz

```bash
cd /path/to/downloaded/files
```

```bash
pip install chess_bot-1.0-py3-none-any.whl
```

or 

```bash
pip install chess_bot-1.0.tar.gz
```
Run by:

```bash
chess-bot
```

## How the AI works

The AI uses a basic decision-making algorithm to evaluate possible moves and select the best one. It analyzes the current board state and computes valid moves based on the rules of chess. The AI operates in a separate process to ensure that the UI remains responsive while the AI is thinking.

## How the AI Finds the Best Move

The Chess AI in this project can find the best move using different algorithms, ranging from simple greedy methods to more advanced techniques like Minimax, NegaMax, and NegaMax with Alpha-Beta Pruning.

### 1. Simple Greedy Method

The **greedy approach** evaluates only the next immediate move and the opponent's best response. It does not look beyond the immediate consequences of the current turn.

- The AI examines all the possible moves the player can make and temporarily makes one.
- It then evaluates the possible responses the opponent can make, scoring each move based on material advantage (piece values).
- The AI selects the move that minimizes the advantage the opponent can gain in their next move, assuming the opponent makes the best possible move.

This approach is **fast** but **short-sighted**, as it doesn’t consider future moves beyond one response from the opponent.

### 2. Minimax Algorithm

The **Minimax algorithm** is a recursive method that simulates all possible moves, not just the immediate ones, looking ahead multiple turns.

- The algorithm assumes that both players are playing optimally.
- It alternates between **minimizing** the opponent's advantage (for the AI's move) and **maximizing** the AI’s advantage (for the opponent’s move).
- Each move is given a score based on the game outcome at the end of the possible series of moves.
  - **Maximizer** (the AI) tries to get the highest score.
  - **Minimizer** (the opponent) tries to minimize the score.
- The algorithm chooses the move that leads to the best possible worst-case scenario.

Minimax is a **deeper** approach, exploring all possible game states up to a certain depth. However, it can be **slow** because it evaluates every possible move.

### 3. NegaMax Algorithm

The **NegaMax algorithm** is a simplified version of Minimax, where instead of alternating between minimizing and maximizing, it negates the evaluation scores based on whose turn it is.

- The game state is scored from the perspective of the player to move. If it's the AI's turn, the score is positive; if it's the opponent's turn, the score is negative.
- Instead of maintaining two functions (maximize and minimize), NegaMax uses a single function and negates the score at each level of recursion.

This approach reduces the complexity of the Minimax implementation, making it easier to write and debug while producing the same results.

### 4. NegaMax Algorithm with Alpha-Beta Pruning

**Alpha-Beta Pruning** is an optimization technique that improves the NegaMax algorithm by eliminating branches in the decision tree that don’t need to be explored.

- It keeps track of two values:
  - **Alpha**: The best value the maximizing player (AI) can guarantee.
  - **Beta**: The best value the minimizing player (opponent) can guarantee.
- During the search, if the AI finds a move that leads to a worse outcome than a previously explored move, it stops evaluating further (this is called **pruning**).
- This reduces the number of moves that need to be evaluated, significantly speeding up the decision-making process.

Alpha-Beta Pruning doesn’t affect the result of the NegaMax algorithm; it just makes it faster by ignoring unpromising branches.

### Summary of Algorithms

| Algorithm                        | Description                                      | Pros                      | Cons                        |
|-----------------------------------|--------------------------------------------------|---------------------------|-----------------------------|
| **Simple Greedy**                 | Evaluates only immediate moves and responses     | Fast                      | Short-sighted, no depth      |
| **Minimax**                       | Recursively evaluates all future moves           | Accounts for future turns  | Slow, explores all branches  |
| **NegaMax**                       | Simplified Minimax, negates scores for opponent  | Easier to implement        | Still slow without pruning   |
| **NegaMax with Alpha-Beta Pruning**| Optimized NegaMax with branch pruning            | Fast, deep lookahead       | Complex to implement         |

These algorithms provide progressively more sophisticated ways of finding the best move, with NegaMax and Alpha-Beta Pruning offering a balance between decision depth and computational efficiency.


## Future improvement

- I want to convert this app into a website where the UI is handled by the client and the server handles the move generation for the AI bot.
- Add multiprocessing for valid move generation to make the app faster.
- Improve the AI by adding more algorithms
- Allow User to save their game progress and add authentication for each user.
- Introduce difficulty mode by adjusting depth values and add an UI for this functionality.

## Project Recording

You can watch the project recording on [here](https://github.com/MSVelan/Chess_AI/blob/main/assets/pjt_recording-1.mkv).

