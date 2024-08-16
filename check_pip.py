#!/usr/bin/env python3

"""
MIT License

Copyright (c) 2024 David Maynor

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Written by David Maynor (dmaynor@gmail.com)
X: @dave_maynor
"""

import os
import sys
import subprocess
import logging

# Configure logging
logging.basicConfig(
    filename='pip_wrapper.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def in_virtualenv():
    """Check if the script is running inside a virtual environment."""
    return (hasattr(sys, 'real_prefix') or
            (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix))

def run_pip_command(args, dry_run=False):
    """Run the pip command with the given arguments."""
    command = ['pip'] + args
    command_str = ' '.join(command)
    
    if dry_run:
        logging.info(f"Dry run: would execute: {command_str}")
        print(f"Dry run: {command_str}")
        return 0

    try:
        logging.info(f"Executing command: {command_str}")
        result = subprocess.run(command, check=True)
        logging.info(f"Command succeeded: {command_str}")
        return result.returncode
    except subprocess.CalledProcessError as e:
        logging.error(f"Command failed with exit code {e.returncode}: {command_str}")
        print(f"Error: {e}")
        return e.returncode
    except Exception as e:
        logging.critical(f"Unexpected error: {e}")
        print(f"Unexpected error: {e}")
        return 1

def print_environment_info():
    """Print and log information about the current environment."""
    logging.info(f"Python executable: {sys.executable}")
    logging.info(f"Virtual environment: {in_virtualenv()}")
    logging.info(f"Environment variables: {os.environ}")
    
    print(f"Python executable: {sys.executable}")
    print(f"Virtual environment: {in_virtualenv()}")
    print("Environment variables:")
    for key, value in os.environ.items():
        print(f"{key}={value}")

def print_help():
    """Print help message."""
    help_message = """
    check_pip.py - A wrapper for pip that alerts if not in a virtual environment.

    MIT License

    Copyright (c) 2024 David Maynor

    Written by David Maynor (dmaynor@gmail.com)
    X: @dave_maynor

    Usage:
      check_pip.py [pip arguments]

    Options:
      --help      Show this help message and exit.
      --dry-run   Simulate the pip command without executing it.
    
    Description:
      This script acts as a wrapper around pip. It alerts you if you are not
      in a virtual environment and logs all pip commands. If the --dry-run
      option is provided, the command is not executed but printed to the console.
    """
    print(help_message)

def main():
    if '--help' in sys.argv:
        print_help()
        sys.exit(0)

    dry_run = '--dry-run' in sys.argv
    if dry_run:
        sys.argv.remove('--dry-run')

    if not in_virtualenv():
        warning_message = "Warning: You are not in a virtual environment!"
        logging.warning(warning_message)
        print(warning_message)
    
    print_environment_info()

    # Pass the arguments to pip
    exit_code = run_pip_command(sys.argv[1:], dry_run=dry_run)
    sys.exit(exit_code)

if __name__ == "__main__":
    main()
