# Tic Tac Toe Unit Tests

This directory contains comprehensive unit tests for the Tic Tac Toe game implementation.

## Test Files

- `test_tic_tac_toe.py` - Main test suite for the TicTacToe class
- `run_tests.py` - Test runner script

## Running Tests

### Using the test runner script:
```bash
python run_tests.py
```

### Using unittest directly:
```bash
python -m unittest test_tic_tac_toe.py -v
```

### Using pytest (if installed):
```bash
python -m pytest test_tic_tac_toe.py -v
```

## Test Coverage

The test suite covers the following functionality:

### Core Game Logic
- **Initialization**: Tests proper game setup with empty board and correct initial state
- **Move Validation**: Tests valid and invalid moves (out of bounds, occupied positions)
- **Move Execution**: Tests making moves and updating the board
- **Player Switching**: Tests alternating between X and O players

### Win Detection
- **Row Wins**: Tests all three rows for winning combinations
- **Column Wins**: Tests all three columns for winning combinations  
- **Diagonal Wins**: Tests both main diagonal and anti-diagonal
- **No Winner**: Tests scenarios with no winning combination

### Game State
- **Board Full Detection**: Tests when the board is completely filled
- **Game Over Conditions**: Tests both win and tie scenarios

### User Input Handling
- **Valid Input**: Tests proper parsing of valid move input
- **Invalid Format**: Tests handling of malformed input
- **Out of Bounds**: Tests input validation for board boundaries
- **Occupied Positions**: Tests handling of moves to already taken positions
- **Quit Commands**: Tests exit functionality ('quit', 'exit', 'q')
- **Error Handling**: Tests keyboard interrupts and value errors

### Game Flow
- **Complete Game with Winner**: Tests full game flow ending in a win
- **Complete Game with Tie**: Tests full game flow ending in a tie
- **Integration**: Tests complete game scenarios with multiple moves

## Test Structure

Each test method follows the Arrange-Act-Assert pattern:
1. **Arrange**: Set up the test conditions (board state, player turn, etc.)
2. **Act**: Execute the method being tested
3. **Assert**: Verify the expected outcomes

## Mocking

The tests use Python's `unittest.mock` to:
- Mock user input to test different scenarios
- Mock print statements to verify output messages
- Mock method calls to isolate specific functionality

## Test Data

The tests include various board configurations to test:
- Empty boards
- Partially filled boards
- Winning combinations
- Tie scenarios
- Edge cases

## Continuous Integration

These tests can be easily integrated into CI/CD pipelines by running:
```bash
python run_tests.py
```

The script exits with code 0 on success and non-zero on failure, making it suitable for automated testing. 