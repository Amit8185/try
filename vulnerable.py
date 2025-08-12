# vulnerable.py

# Example of a hardcoded password (Semgrep will catch this)


def login(user, pwd):
    if user == "admin" and pwd == "1234":
        return "Access granted"
    return "Access denied"
