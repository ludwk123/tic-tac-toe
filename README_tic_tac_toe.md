# Tic Tac Toe Game 🎮

A simple, interactive command-line tic-tac-toe game written in Python for two players.

## Features

- **Interactive Gameplay**: Clean command-line interface with visual board display
- **Input Validation**: Robust error handling for invalid moves and inputs
- **Win Detection**: Automatic detection of wins, ties, and game completion
- **Replay Option**: Play multiple games in a session
- **User-Friendly**: Clear instructions and helpful error messages
- **Graceful Exit**: Type 'quit' anytime to exit or use Ctrl+C

## How to Play

1. **Start the Game**: Run the Python script
2. **Make Moves**: Players take turns entering their moves
3. **Input Format**: Enter moves as "row col" (e.g., "1 2" for row 1, column 2)
4. **Win Conditions**: Get three in a row horizontally, vertically, or diagonally
5. **Game End**: The game announces the winner or declares a tie

## Installation & Running

### Prerequisites
- Python 3.6 or higher

### Running the Game
```bash
python3 tic_tac_toe.py
```

Or make it executable and run directly:
```bash
chmod +x tic_tac_toe.py
./tic_tac_toe.py
```

## Game Interface

The game displays a numbered grid:
```
   1   2   3
1    |   |  
  -----------
2    |   |  
  -----------
3    |   |  
```

Players enter coordinates as numbers (1-3 for both row and column).

## Example Gameplay

```
🎮 Welcome to Tic Tac Toe! 🎮
Enter moves as 'row col' (e.g., '1 2' for row 1, column 2)
Type 'quit' to exit the game

   1   2   3
1    |   |  
  -----------
2    |   |  
  -----------
3    |   |  

Player X, enter your move (row col): 1 1

   1   2   3
1  X |   |  
  -----------
2    |   |  
  -----------
3    |   |  

Player O, enter your move (row col): 2 2
```

## Game Controls

- **Make a Move**: Enter "row col" (e.g., "1 3", "2 1")
- **Quit Game**: Type "quit", "exit", "q", or press Ctrl+C
- **Play Again**: After a game ends, choose 'y' to play again or 'n' to exit

## Code Structure

The game is implemented using object-oriented programming:

- **TicTacToe Class**: Main game logic and state management
- **Board Management**: 3x3 grid representation and display
- **Input Validation**: Ensures valid moves and handles errors
- **Win Detection**: Checks rows, columns, and diagonals
- **Game Loop**: Manages turn-based gameplay and replay functionality

## Error Handling

The game handles various error conditions:
- Invalid coordinate inputs
- Moves to occupied positions
- Out-of-range coordinates
- Non-numeric inputs
- Keyboard interrupts (Ctrl+C)

## License

This project is open source and available under the MIT License.

## Contributing

Feel free to fork this project and submit pull requests for improvements!
