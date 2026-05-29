# Quiz Game Application
# This script asks a series of questions, tracks the score, and provides feedback based on performance.
# Functions are used to encapsulate each question for modularity.

def ask_question(question: str, options: list, correct_option: str) -> bool:
    """Prompt the user with a multiple‑choice question.
    Returns True if the answer is correct, otherwise False.
    """
    print("\n" + question)
    for idx, opt in enumerate(options, start=1):
        print(f"{idx}. {opt}")
    while True:
        try:
            answer = int(input("Your answer (enter the option number): "))
            if 1 <= answer <= len(options):
                break
            else:
                print(f"Please enter a number between 1 and {len(options)}.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    return options[answer - 1].lower() == correct_option.lower()


def main():
    # Define a list of questions. Each entry is a tuple:
    # (question_text, [option1, option2, ...], correct_option_text)
    questions = [
        ("What is the capital of France?", ["Berlin", "Paris", "Rome", "Madrid"], "Paris"),
        ("Which language is primarily used for web development?", ["Python", "Java", "JavaScript", "C++"], "JavaScript"),
        ("What is 5 * 6?", ["30", "11", "56", "20"], "30"),
        ("Who wrote 'Hamlet'?", ["Charles Dickens", "William Shakespeare", "Mark Twain", "J.K. Rowling"], "William Shakespeare"),
        ("Which planet is known as the Red Planet?", ["Mars", "Venus", "Jupiter", "Saturn"], "Mars"),
    ]

    score = 0
    for q_text, opts, correct in questions:
        if ask_question(q_text, opts, correct):
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer was: {correct}")
            # Bonus: negative marking (deduct 0.5 point per wrong answer)
            score -= 0.5

    # Ensure score does not drop below zero
    if score < 0:
        score = 0

    print("\n--- Quiz Completed ---")
    print(f"Your final score is: {score}/{len(questions)}")

    # Feedback based on score
    if score > 4:
        print("Excellent")
    elif 3 <= score <= 4:
        print("Good")
    else:
        print("Needs Practice")

if __name__ == "__main__":
    main()
