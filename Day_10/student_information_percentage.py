# Student Information & Percentage Calculator
# This script collects a student's name, roll number, and marks for five subjects.
# It then calculates total marks, average, percentage and prints a performance message.

def get_student_details():
    """Prompt user for basic details and marks for 5 subjects."""
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    marks = []
    for i in range(1, 6):
        while True:
            try:
                mark = float(input(f"Enter marks for subject {i} (0-100): "))
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Marks should be between 0 and 100.")
            except ValueError:
                print("Please enter a valid number.")
    return name, roll, marks


def calculate_statistics(marks):
    total = sum(marks)
    average = total / len(marks)
    percentage = (total / (len(marks) * 100)) * 100
    return total, average, percentage


def performance_message(percentage):
    if percentage > 90:
        return "Excellent"
    elif 75 <= percentage <= 90:
        return "Very Good"
    else:
        return "Needs Improvement"


def main():
    name, roll, marks = get_student_details()
    total, average, percentage = calculate_statistics(marks)
    message = performance_message(percentage)
    print("\n--- Student Report ---")
    print(f"Name       : {name}")
    print(f"Roll No.   : {roll}")
    for idx, m in enumerate(marks, start=1):
        print(f"Subject {idx} : {m}")
    print(f"Total      : {total}")
    print(f"Average    : {average:.2f}")
    print(f"Percentage : {percentage:.2f}%")
    print(f"Performance: {message}")

if __name__ == "__main__":
    main()
