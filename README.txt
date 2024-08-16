===============================================================================
                            check_pip.py README
===============================================================================

Description:
-------------
`check_pip.py` is a Python script that acts as a wrapper around `pip`. It alerts
you if you are not in a virtual environment, ensuring that you maintain best 
practices when managing Python dependencies. The script also provides logging,
dry run capabilities, and detailed information about the current environment.

Author:
--------
Written by: David Maynor
Email: dmaynor@gmail.com
X (Twitter): @dave_maynor

License:
--------
This script is licensed under the MIT License. For more information, see the
license header in the script file.

Features:
---------
1. **Virtual Environment Check**:
   - Alerts if the script is not running within a virtual environment.

2. **Logging**:
   - Logs all commands and significant events to `pip_wrapper.log` for auditing.

3. **Dry Run Mode**:
   - Use the `--dry-run` flag to simulate the pip command without actually 
     executing it. This is useful for testing or verifying what the command will do.

4. **Environment Transparency**:
   - Prints and logs details about the current Python executable, whether 
     you are in a virtual environment, and the environment variables.

5. **Help Command**:
   - Use the `--help` flag to display a detailed help message explaining the 
     script's usage, options, and functionality.

Usage:
------
1. To install a package:
