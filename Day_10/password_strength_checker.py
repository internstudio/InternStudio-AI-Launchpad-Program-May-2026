# Password Strength Checker
# This script evaluates a password's strength based on length and character composition.
# Strength levels: Weak, Medium, Strong.
# Bonus: Repeats prompting until a Strong password is entered.

import re

def assess_strength(password: str) -> str:
    """Return strength classification for the given password.

    Criteria:
    - Weak: does not meet medium criteria.
    - Medium: length >=8 and meets at least two of the three character rules.
    - Strong: length >=8 and meets all three character rules.
    """
    length_ok = len(password) >= 8
    has_upper = bool(re.search(r"[A-Z]", password))
    has_lower = bool(re.search(r"[a-z]", password))
    has_digit = bool(re.search(r"[0-9]", password))

    # Count how many of the character rules are satisfied
    rules_met = sum([has_upper, has_lower, has_digit])

    if not length_ok or rules_met < 2:
        return "Weak Password"
    if rules_met == 2:
        return "Medium Password"
    return "Strong Password"

def main():
    while True:
        pwd = input("Enter a password to check its strength: ")
        strength = assess_strength(pwd)
        print(strength)
        if strength == "Strong Password":
            print("Your password is strong enough.")
            break
        else:
            print("Please try again with a stronger password.\n")

if __name__ == "__main__":
    main()
