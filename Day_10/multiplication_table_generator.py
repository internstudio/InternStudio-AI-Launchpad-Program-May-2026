# Multiplication Table Generator
# This script prompts the user for a number and a limit, then prints the multiplication
# table for that number up to the given limit. Optional bonus prints tables from 1
# to the entered number.

def generate_table(number, limit):
    for i in range(1, limit + 1):
        print(f"{number} x {i} = {number * i}")


def bonus_multiple_tables(upto, limit):
    for n in range(1, upto + 1):
        print(f"\nMultiplication Table for {n}:")
        generate_table(n, limit)


def main():
    try:
        num = int(input("Enter the number for which you want the table: "))
        lim = int(input("Enter how many multiples to print: "))
    except ValueError:
        print("Please enter valid integers.")
        return
    print("\n--- Multiplication Table ---")
    generate_table(num, lim)
    # Bonus: ask if user wants tables from 1 to the entered number
    resp = input("Do you want tables from 1 to the entered number? (y/n): ").strip().lower()
    if resp == 'y':
        bonus_multiple_tables(num, lim)

if __name__ == "__main__":
    main()
