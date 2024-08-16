Explanation:

	1.	Virtual Environment Check:
	•	The in_virtualenv() function determines if the script is running inside a virtual environment. It checks for the presence of sys.real_prefix or compares sys.base_prefix and sys.prefix.
	2.	Running the pip Command:
	•	The run_pip_command() function executes the pip command with the arguments passed to the script. It uses subprocess.run() to run the command and capture the result.
	3.	Main Execution:
	•	The main() function checks if you’re in a virtual environment. If not, it prints a warning message.
	•	The script then passes the command-line arguments to pip using the run_pip_command() function.
	4.	Shebang:
	•	The script starts with the #!/usr/bin/env python3 shebang, making it executable in a Unix-like environment.

Usage:

	1.	Save the script as check_pip.py.
	2.	Make the script executable:

chmod +x check_pip.py


	3.	Run the script with the same arguments you would use with pip:

./check_pip.py install requests
