# Tic Tac Toe Unit Tests

This directory contains comprehensive unit tests for the Tic Tac Toe game implementation.

## Test Files

- `test_tic_tac_toe.py` - Main test suite for the TicTacToe class
- `run_tests.py` - Test runner script with a nice interface

## Running Tests

### Option 1: Using the test runner (recommended)
```bash
python run_tests.py
```

### Option 2: Using unittest directly
```bash
python -m unittest test_tic_tac_toe.py -v
```

### Option 3: Running individual test methods
```bash
python -m unittest test_tic_tac_toe.TestTicTacToe.test_initialization -v
```

## Test Coverage

The test suite covers all major functionality of the TicTacToe class:

### Core Game Logic
- ✅ **Initialization** - Tests proper game state setup
- ✅ **Valid/Invalid Moves** - Tests move validation (bounds, occupied positions)
- ✅ **Making Moves** - Tests successful and failed move attempts
- ✅ **Player Switching** - Tests alternating between X and O players

### Win Detection
- ✅ **Row Wins** - Tests all three rows for winning combinations
- ✅ **Column Wins** - Tests all three columns for winning combinations
- ✅ **Diagonal Wins** - Tests both main and anti-diagonals
- ✅ **No Winner** - Tests scenarios with no winning condition

### Game State
- ✅ **Board Full Detection** - Tests tie game scenarios
- ✅ **Complete Game Flow** - Tests a full game from start to win
- ✅ **Tie Game** - Tests scenarios where the board fills without a winner

### User Interface
- ✅ **Board Display** - Tests the visual output of the game board
- ✅ **Player Input Validation** - Tests various input scenarios:
  - Valid input format
  - Invalid format (wrong number of values)
  - Out-of-bounds values
  - Occupied positions
  - Quit/exit commands
  - Keyboard interrupts

## Test Statistics

- **Total Tests**: 19
- **Test Categories**: 8
- **Coverage**: All public methods of TicTacToe class
- **Edge Cases**: Comprehensive coverage of error conditions

## Test Structure

Each test method follows a clear pattern:
1. **Setup** - Prepare test data and game state
2. **Action** - Execute the method being tested
3. **Assertion** - Verify expected outcomes

## Mocking

The tests use Python's `unittest.mock` to:
- Mock user input for testing the `get_player_input()` method
- Capture stdout to test the `display_board()` method
- Handle system exits for quit/exit scenarios

## Example Test Output

```
🧪 Running Tic Tac Toe Unit Tests 🧪
==================================================
test_initialization (test_tic_tac_toe.TestTicTacToe)
Test that the game initializes correctly. ... ok
test_is_valid_move (test_tic_tac_toe.TestTicTacToe)
Test valid and invalid moves. ... ok
...
----------------------------------------------------------------------
Ran 19 tests in 0.005s

OK
==================================================
✅ All tests passed! ✅
```

## Adding New Tests

To add new tests:

1. Add test methods to the `TestTicTacToe` class in `test_tic_tac_toe.py`
2. Follow the naming convention: `test_<method_name>_<scenario>`
3. Include docstrings explaining what the test covers
4. Run the test suite to ensure all tests pass

## Best Practices

- Each test should be independent and not rely on other tests
- Use descriptive test names that explain the scenario being tested
- Test both valid and invalid inputs
- Test edge cases and error conditions
- Keep tests focused on a single piece of functionality 