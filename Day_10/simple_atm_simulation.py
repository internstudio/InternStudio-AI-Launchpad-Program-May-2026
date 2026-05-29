# Simple ATM Machine Simulation
# This script simulates a basic ATM with PIN verification, balance inquiry,
# deposits, and withdrawals. It limits to 3 incorrect PIN attempts.

def atm_simulation():
    DEFAULT_PIN = "1234"
    balance = 1000.0  # default account balance
    attempts = 0
    max_attempts = 3

    while attempts < max_attempts:
        pin = input("Enter your PIN: ")
        if pin == DEFAULT_PIN:
            break
        else:
            attempts += 1
            print(f"Incorrect PIN. Attempts left: {max_attempts - attempts}")
    else:
        print("Account Locked")
        return

    while True:
        print("\n--- ATM Menu ---")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        choice = input("Select an option (1-4): ")
        if choice == "1":
            print(f"Your current balance is: ₹{balance:.2f}")
        elif choice == "2":
            try:
                amount = float(input("Enter amount to deposit: ₹"))
                if amount > 0:
                    balance += amount
                    print(f"Deposit successful. New balance: ₹{balance:.2f}")
                else:
                    print("Enter a positive amount.")
            except ValueError:
                print("Invalid amount.")
        elif choice == "3":
            try:
                amount = float(input("Enter amount to withdraw: ₹"))
                if amount > balance:
                    print("Insufficient Balance")
                elif amount <= 0:
                    print("Enter a positive amount.")
                else:
                    balance -= amount
                    print(f"Withdrawal successful. New balance: ₹{balance:.2f}")
            except ValueError:
                print("Invalid amount.")
        elif choice == "4":
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    atm_simulation()
