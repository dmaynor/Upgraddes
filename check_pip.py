#!/usr/bin/env python3

import os
import sys
import subprocess

def in_virtualenv():
    """Check if the script is running inside a virtual environment."""
    return (hasattr(sys, 'real_prefix') or
            (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix))

def run_pip_command(args):
    """Run the pip command with the given arguments."""
    try:
        result = subprocess.run(['pip'] + args, check=True)
        return result.returncode
    except subprocess.CalledProcessError as e:
        return e.returncode

def main():
    if not in_virtualenv():
        print("Warning: You are not in a virtual environment!")
        print("It's recommended to use pip within a virtual environment.")
        # You can choose to exit here if you don't want to proceed
        # sys.exit(1)
    
    # Pass the arguments to pip
    exit_code = run_pip_command(sys.argv[1:])
    sys.exit(exit_code)

if __name__ == "__main__":
    main()
