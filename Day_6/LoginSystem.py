correct_username = "admin"
correct_password = "python123"

secret_code = "ADMIN2026"

# Maximum login attempts
max_attempts = 3

# Counter
attempt = 0

print("===== Welcome to Secure Login System =====")

# Loop for login attempts
while attempt < max_attempts:

    print(f"\nLogin Attempt {attempt + 1}")

    # User input
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    # Password length validation
    if len(password) < 6:
        print("Password must contain at least 6 characters.")
        continue

    # Secret admin code check
    admin_code = input("Enter Secret Admin Code: ")

    # Check credentials
    if (
        username == correct_username
        and password == correct_password
        and admin_code == secret_code
    ):

        print("\nLogin Successful")

        # Greeting message
        if username == "admin":
            print("Welcome Admin!")
            print("You have full system access.")

        break

    else:
        attempt += 1

        remaining = max_attempts - attempt

        print("\nInvalid Username, Password, or Secret Code")

        # Failed attempt message
        if remaining > 0:
            print(f"Attempts Remaining: {remaining}")

# Account locked
if attempt == max_attempts:
    print("\nAccount Locked")
    print("Too many failed login attempts.")