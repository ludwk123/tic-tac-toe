# Coverage Reporting for Tic Tac Toe

This project now includes comprehensive test coverage reporting using `coverage.py`.

## Installation

First, install the coverage package:

```bash
pip install -r requirements.txt
```

Or install coverage directly:

```bash
pip install coverage
```

## Running Tests with Coverage

### Option 1: Using the Custom Coverage Runner

```bash
python run_tests_with_coverage.py
```

This will:
- Run all tests
- Generate a console coverage report
- Create an HTML report in the `htmlcov/` directory
- Create an XML report (`coverage.xml`)

### Option 2: Using the Simple Coverage Runner

```bash
python run_coverage.py
```

This uses the standard coverage.py command-line interface.

### Option 3: Using Coverage Commands Directly

```bash
# Run tests with coverage
coverage run --source=tic_tac_toe.py run_tests.py

# Generate console report
coverage report

# Generate HTML report
coverage html

# Generate XML report
coverage xml
```

## Coverage Reports

### Console Report
Shows a summary of coverage statistics including:
- Lines covered
- Lines missing
- Branch coverage
- Percentage coverage

### HTML Report
A detailed, interactive HTML report is generated in the `htmlcov/` directory. Open `htmlcov/index.html` in your browser to see:
- File-by-file coverage breakdown
- Line-by-line coverage highlighting
- Missing lines highlighted in red
- Covered lines highlighted in green

### XML Report
The `coverage.xml` file can be used by CI/CD systems and coverage reporting tools.

## Configuration

The `.coveragerc` file configures coverage settings:

- **Source files**: Only `tic_tac_toe.py` is measured
- **Excluded files**: Test files, runner scripts, and cache directories
- **Excluded lines**: Common patterns like debug code, abstract methods, etc.

## Coverage Goals

- **Target**: Aim for 90%+ line coverage
- **Focus**: Ensure all game logic paths are tested
- **Quality**: High coverage should indicate comprehensive testing

## Interpreting Coverage

### High Coverage Areas
- Game initialization
- Move validation
- Win detection
- Player switching

### Areas to Watch
- Edge cases in input handling
- Game termination conditions
- Error handling paths

## Continuous Integration

For CI/CD systems, the XML report can be used:

```yaml
# Example GitHub Actions step
- name: Run tests with coverage
  run: |
    pip install coverage
    coverage run --source=tic_tac_toe.py run_tests.py
    coverage xml
    coverage report
```

## Troubleshooting

### Coverage Not Working
1. Ensure `coverage` is installed: `pip install coverage`
2. Check that `tic_tac_toe.py` exists in the current directory
3. Verify test files follow the `test_*.py` pattern

### Missing Coverage Data
- Make sure tests are actually running
- Check that the source file is being imported during tests
- Verify the `.coveragerc` configuration

### HTML Report Not Generated
- Check that the `htmlcov/` directory is writable
- Ensure coverage data was collected (look for `.coverage` file)

## Files Added

- `requirements.txt` - Dependencies
- `run_tests_with_coverage.py` - Custom coverage runner
- `run_coverage.py` - Simple coverage runner
- `.coveragerc` - Coverage configuration
- `README_COVERAGE.md` - This documentation 