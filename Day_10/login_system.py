# Username & Password Login System
# This script implements a simple login system with a maximum of 3 attempts.
# It also provides a special welcome for the user "admin" and validates password length.

USERNAME = "user123"
PASSWORD = "passw0rd"
MAX_ATTEMPTS = 3


def login():
    attempts = 0
    while attempts < MAX_ATTEMPTS:
        entered_user = input("Enter username: ")
        entered_pass = input("Enter password: ")
        if entered_user == USERNAME and entered_pass == PASSWORD:
            if entered_user.lower() == "admin":
                print("Welcome, admin! You have full access.")
            else:
                print("Login Successful")
            return True
        else:
            attempts += 1
            remaining = MAX_ATTEMPTS - attempts
            print(f"Invalid Username or Password. Attempts left: {remaining}")
            # Bonus: password length validation feedback
            if len(entered_pass) < 6:
                print("Note: Password should be at least 6 characters long.")
    print("Account Locked: Too many failed attempts.")
    return False

if __name__ == "__main__":
    login()
