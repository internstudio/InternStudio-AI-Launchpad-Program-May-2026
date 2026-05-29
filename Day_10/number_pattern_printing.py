# Number Pattern Printing Program
# This script prints two patterns as described in the requirements.

def pattern_one(n=5):
    """Prints pattern:
    1
    12
    123
    ... up to n
    """
    for i in range(1, n + 1):
        line = ''.join(str(j) for j in range(1, i + 1))
        print(line)


def pattern_two(start=5):
    """Prints pattern:
    54321
    5432
    543
    54
    5
    """
    for i in range(start, 0, -1):
        line = ''.join(str(j) for j in range(start, i - 1, -1))
        print(line)


def main():
    print("Pattern 1:")
    pattern_one()
    print("\nPattern 2:")
    pattern_two()
    # Bonus: custom pattern example
    print("\nCustom Pattern (example - pyramid of *):")
    rows = 5
    for i in range(1, rows + 1):
        print(' ' * (rows - i) + '* ' * i)

if __name__ == "__main__":
    main()
