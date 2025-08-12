import subprocess

def run_command(user_input):
    # Dangerous use of shell=True leading to command injection vulnerability
    subprocess.call(user_input, shell=True)
