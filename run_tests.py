#!/usr/bin/env python3
"""
Test runner for Tic Tac Toe Game
Provides a simple interface to run all unit tests.
"""

import unittest
import sys
import os

def run_tests():
    """Run all unit tests for the Tic Tac Toe game."""
    print("🧪 Running Tic Tac Toe Unit Tests 🧪")
    print("=" * 50)
    
    # Add the current directory to the Python path
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    
    # Discover and run tests
    loader = unittest.TestLoader()
    start_dir = os.path.dirname(os.path.abspath(__file__))
    suite = loader.discover(start_dir, pattern='test_*.py')
    
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    print("\n" + "=" * 50)
    if result.wasSuccessful():
        print("✅ All tests passed! ✅")
        return 0
    else:
        print("❌ Some tests failed! ❌")
        return 1

if __name__ == '__main__':
    sys.exit(run_tests()) 