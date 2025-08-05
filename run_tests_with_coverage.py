#!/usr/bin/env python3
"""
Test runner for Tic Tac Toe unit tests with coverage reporting
"""

import unittest
import sys
import os
import coverage

def run_tests_with_coverage():
    """Run tests with coverage reporting."""
    
    # Start coverage measurement
    cov = coverage.Coverage(
        omit=[
            '*/test_*.py',
            '*/run_tests*.py',
            '*/generate_test_report.py',
            '*/__pycache__/*'
        ]
    )
    cov.start()
    
    # Discover and run all tests
    loader = unittest.TestLoader()
    start_dir = '.'
    suite = loader.discover(start_dir, pattern='test_*.py')
    
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Stop coverage measurement
    cov.stop()
    cov.save()
    
    # Generate coverage report
    print("\n" + "="*60)
    print("COVERAGE REPORT")
    print("="*60)
    
    # Print summary to console
    cov.report()
    
    # Generate HTML report
    cov.html_report(directory='htmlcov')
    print(f"\nHTML coverage report generated in 'htmlcov' directory")
    print(f"Open 'htmlcov/index.html' in your browser to view detailed coverage")
    
    # Generate XML report (useful for CI/CD)
    cov.xml_report(outfile='coverage.xml')
    print(f"XML coverage report generated as 'coverage.xml'")
    
    # Exit with appropriate code
    return result.wasSuccessful()

if __name__ == '__main__':
    success = run_tests_with_coverage()
    sys.exit(not success) 