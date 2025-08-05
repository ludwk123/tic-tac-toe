#!/usr/bin/env python3
"""
Simple coverage runner using coverage.py command line interface
"""

import subprocess
import sys
import os

def run_coverage():
    """Run tests with coverage using coverage.py CLI."""
    
    # Run coverage
    result = subprocess.run([
        sys.executable, '-m', 'coverage', 'run', 
        '--source=tic_tac_toe',
        'run_tests.py'
    ], capture_output=True, text=True)
    
    # Print test output
    print(result.stdout)
    if result.stderr:
        print("STDERR:", result.stderr)
    
    # Generate reports
    subprocess.run([sys.executable, '-m', 'coverage', 'report'])
    subprocess.run([sys.executable, '-m', 'coverage', 'html'])
    subprocess.run([sys.executable, '-m', 'coverage', 'xml'])
    
    print("\nCoverage reports generated:")
    print("- Console report above")
    print("- HTML report: htmlcov/index.html")
    print("- XML report: coverage.xml")
    
    return result.returncode == 0

if __name__ == '__main__':
    success = run_coverage()
    sys.exit(not success) 