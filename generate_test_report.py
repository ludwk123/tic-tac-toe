#!/usr/bin/env python3
"""
Test Report Generator for Tic-Tac-Toe
Automatically generates comprehensive test reports
"""

import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path


def run_tests():
    """Run the test suite and capture output."""
    print("Running tests...")
    start_time = time.time()
    
    try:
        result = subprocess.run(
            [sys.executable, 'run_tests.py'],
            capture_output=True,
            text=True,
            timeout=30
        )
        execution_time = time.time() - start_time
        return result, execution_time
    except subprocess.TimeoutExpired:
        print("❌ Tests timed out after 30 seconds")
        return None, 30
    except Exception as e:
        print(f"❌ Error running tests: {e}")
        return None, 0


def parse_test_results(output):
    """Parse test output to extract results."""
    lines = output.split('\n')
    test_count = 0
    failed_tests = []
    
    for line in lines:
        if line.strip().startswith('test_') and '... ok' in line:
            test_count += 1
        elif line.strip().startswith('test_') and '... FAIL' in line:
            test_count += 1
            failed_tests.append(line.split('...')[0].strip())
    
    return test_count, failed_tests


def generate_report(test_result, execution_time):
    """Generate the test report."""
    if test_result is None:
        return generate_error_report()
    
    output = test_result.stdout
    return_code = test_result.returncode
    
    test_count, failed_tests = parse_test_results(output)
    success = return_code == 0
    
    report = f"""# Tic-Tac-Toe Test Report

## Executive Summary

**Date:** {datetime.now().strftime('%B %Y')}  
**Project:** Tic-Tac-Toe Game  
**Test Framework:** Python unittest  
**Total Tests:** {test_count}  
**Test Status:** {'✅ ALL TESTS PASSING' if success else '❌ TESTS FAILED'}  
**Execution Time:** {execution_time:.3f}s  

## Test Results

### Overall Status
- **Success Rate:** {((test_count - len(failed_tests)) / max(test_count, 1) * 100):.1f}% ({test_count - len(failed_tests)}/{test_count})
- **Failed Tests:** {len(failed_tests)}
- **Execution Time:** {execution_time:.3f} seconds

"""

    if failed_tests:
        report += f"""
### Failed Tests
{chr(10).join(f"- {test}" for test in failed_tests)}

"""

    report += f"""
## Test Output

```
{output}
```

## Recommendations

"""

    if success:
        report += """✅ **All tests are passing!** 

### Immediate Actions
- No immediate actions required

### Future Enhancements
1. Add coverage reporting with coverage.py
2. Add performance benchmarks
3. Consider adding stress tests
4. Add cross-platform testing
"""
    else:
        report += """❌ **Some tests are failing!**

### Immediate Actions
1. Review failed tests above
2. Fix failing test cases
3. Re-run tests to verify fixes
4. Update test documentation if needed

### Common Issues
- Check for syntax errors in test files
- Verify test dependencies are installed
- Ensure test environment is properly configured
"""

    report += f"""
## Report Generation

- **Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
- **Test Runner:** {sys.executable}
- **Python Version:** {sys.version.split()[0]}
"""

    return report


def generate_error_report():
    """Generate a report when tests fail to run."""
    return f"""# Tic-Tac-Toe Test Report

## Executive Summary

**Date:** {datetime.now().strftime('%B %Y')}  
**Project:** Tic-Tac-Toe Game  
**Status:** ❌ **TEST EXECUTION FAILED**  

## Error Details

The test suite failed to execute properly. This could be due to:

1. **Missing Dependencies**: Required packages not installed
2. **Syntax Errors**: Errors in test or source code
3. **Environment Issues**: Python version or path problems
4. **File Permissions**: Unable to access test files

## Recommendations

### Immediate Actions
1. Check Python installation and version
2. Verify all required files exist
3. Run tests manually to identify specific errors
4. Check for syntax errors in source code

### Troubleshooting Steps
1. Run `python3 run_tests.py` manually
2. Check for import errors
3. Verify file permissions
4. Review error messages for specific issues

## Report Generation

- **Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
- **Error:** Test execution failed
"""


def main():
    """Main function to generate test report."""
    print("🧪 Generating Tic-Tac-Toe Test Report...")
    
    # Run tests
    test_result, execution_time = run_tests()
    
    # Generate report
    report = generate_report(test_result, execution_time)
    
    # Write report to file
    report_file = Path('TEST_REPORT.md')
    report_file.write_text(report)
    
    print(f"📊 Test report generated: {report_file}")
    print(f"⏱️  Execution time: {execution_time:.3f}s")
    
    if test_result and test_result.returncode == 0:
        print("✅ All tests passed!")
    elif test_result:
        print("❌ Some tests failed. Check the report for details.")
    else:
        print("❌ Test execution failed. Check the report for details.")


if __name__ == "__main__":
    main() 