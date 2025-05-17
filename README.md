
# TicTacToe AI

A Python implementation of Tic Tac Toe featuring an unbeatable AI powered by the Minimax algorithm and a graphical user interface built with Pygame.

## Features

- **Play as X or O:** Choose your player and challenge the computer.
- **Smart AI:** The computer uses the Minimax algorithm to always play optimally.
- **Graphical Interface:** Clean interface using Pygame for an interactive experience.
- **Replayable:** Restart and play as many times as you wish.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/KamogeloMahlake/tictactoe-ai.git
   cd tictactoe-ai
   ```

2. **Install dependencies:**
   Ensure you have Python 3 installed, then install Pygame:
   ```bash
   pip install pygame
   ```

3. **Font requirement:**
   Make sure the file `OpenSans-Regular.ttf` is present in the project directory.  
   (You can download it from [Google Fonts](https://fonts.google.com/specimen/Open+Sans) if needed.)

## How to Run

1. After installing dependencies and ensuring the font file is in place, start the game with:
   ```bash
   python runner.py
   ```

## How It Works

- On startup, the game prompts you to choose to play as X or O.
- The board is displayed, and you make moves by clicking on the desired tile.
- The AI opponent calculates its moves using the minimax algorithm to ensure it cannot be beaten.
- When the game ends (win or tie), you can play again by clicking the **Play Again** button.

## Code Structure

### `tictactoe.py`

Implements the game logic and the AI:
- **initial_state:** Returns the starting state of the board.
- **player:** Determines whose turn it is.
- **actions:** Lists all valid moves.
- **result:** Returns the board after a move.
- **winner:** Checks if there is a winner.
- **terminal:** Checks if the game is over.
- **utility:** Returns the utility value of the board (`1`: X wins, `-1`: O wins, `0`: tie).
- **minimax:** Determines the optimal move for the current player.
- **min_value / max_value:** Helper functions for the minimax algorithm.

### `runner.py`

Handles the Pygame UI and user interaction:
- Draws the game board and interface elements.
- Handles user input (mouse clicks).
- Calls the AI for computer moves.
- Displays the game outcome and allows replaying.
