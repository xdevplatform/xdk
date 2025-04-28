#!/usr/bin/env python3
import argparse
import pytest
import sys
from pathlib import Path
from get_tweets_success import test_get_tweets

def run_tests(verbose=False):
    """
    Run the test suite with optional verbose output.
    
    Args:
        verbose (bool): If True, print detailed test responses
    """
    # Store the verbose flag in a module-level variable
    sys.modules['get_tweets_success'].VERBOSE = verbose
    
    # Run pytest with appropriate arguments
    pytest_args = [__file__]
    if verbose:
        pytest_args.extend(['-v', '-s'])
    
    return pytest.main(pytest_args)

def main():
    parser = argparse.ArgumentParser(description='XDK Test Orchestrator')
    parser.add_argument('-v', '--verbose', action='store_true',
                      help='Enable verbose output to print test responses')
    
    args = parser.parse_args()
    
    # Run the tests
    exit_code = run_tests(verbose=args.verbose)
    sys.exit(exit_code)

if __name__ == '__main__':
    main() 