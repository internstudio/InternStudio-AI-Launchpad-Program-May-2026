# Odd and Even Number Analyzer
# This script asks for a start and end range, then prints even and odd numbers,
# counts them, and optionally sums even numbers.

def get_range():
    while True:
        try:
            start = int(input("Enter the starting number: "))
            end = int(input("Enter the ending number: "))
            if start > end:
                print("Starting number should be less than or equal to ending number.")
                continue
            return start, end
        except ValueError:
            print("Please enter valid integers.")


def analyze_numbers(start, end):
    even_numbers = []
    odd_numbers = []
    for num in range(start, end + 1):
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)
    return even_numbers, odd_numbers


def main():
    start, end = get_range()
    evens, odds = analyze_numbers(start, end)
    print("\nEven numbers:")
    print(evens)
    print("Count of even numbers:", len(evens))
    print("\nOdd numbers:")
    print(odds)
    print("Count of odd numbers:", len(odds))
    # Bonus: sum of even numbers
    sum_even = sum(evens)
    print("\nSum of even numbers:", sum_even)

if __name__ == "__main__":
    main()
