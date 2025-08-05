#!/usr/bin/env python3
"""
Demonstration of coverage reporting features
"""

import subprocess
import sys
import os

def demo_coverage():
    """Demonstrate coverage reporting features."""
    
    print("🎯 Tic Tac Toe Coverage Demo 🎯")
    print("=" * 50)
    
    # Check if coverage is installed
    try:
        import coverage
        print("✅ Coverage package is installed")
    except ImportError:
        print("❌ Coverage package not found. Install with: pip3 install coverage")
        return False
    
    # Run tests with coverage
    print("\n📊 Running tests with coverage...")
    result = subprocess.run([
        sys.executable, '-m', 'coverage', 'run', 
        '--source=tic_tac_toe',
        'run_tests.py'
    ], capture_output=True, text=True)
    
    if result.returncode == 0:
        print("✅ Tests passed!")
    else:
        print("❌ Tests failed!")
        print(result.stderr)
        return False
    
    # Generate and display coverage report
    print("\n📈 Coverage Report:")
    print("-" * 30)
    
    report_result = subprocess.run([
        sys.executable, '-m', 'coverage', 'report'
    ], capture_output=True, text=True)
    
    print(report_result.stdout)
    
    # Show missing lines
    print("\n🔍 Missing Coverage Lines:")
    print("-" * 30)
    
    missing_result = subprocess.run([
        sys.executable, '-m', 'coverage', 'report', '--show-missing'
    ], capture_output=True, text=True)
    
    print(missing_result.stdout)
    
    # Generate HTML report
    print("\n🌐 Generating HTML report...")
    html_result = subprocess.run([
        sys.executable, '-m', 'coverage', 'html'
    ], capture_output=True, text=True)
    
    if html_result.returncode == 0:
        print("✅ HTML report generated in 'htmlcov/index.html'")
        print("   Open this file in your browser to see detailed coverage")
    else:
        print("❌ Failed to generate HTML report")
    
    # Generate XML report
    print("\n📄 Generating XML report...")
    xml_result = subprocess.run([
        sys.executable, '-m', 'coverage', 'xml'
    ], capture_output=True, text=True)
    
    if xml_result.returncode == 0:
        print("✅ XML report generated as 'coverage.xml'")
    else:
        print("❌ Failed to generate XML report")
    
    print("\n🎉 Coverage demo completed!")
    print("\n📋 Available commands:")
    print("  python3 run_coverage.py          - Run tests with coverage")
    print("  python3 -m coverage run --source=tic_tac_toe run_tests.py")
    print("  python3 -m coverage report       - Show coverage summary")
    print("  python3 -m coverage html         - Generate HTML report")
    print("  python3 -m coverage xml          - Generate XML report")
    
    return True

if __name__ == '__main__':
    demo_coverage() 