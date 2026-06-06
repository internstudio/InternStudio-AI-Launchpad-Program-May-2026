# The pupose of this project is to provide quiz appliation

# total questions 20
# dictonary
questions = {
    "question1": {
        "text": "What is the correct file extension for Python files?",
        "options": [".py", ".pt", ".python", ".p"],
        "correct": 0
    },
    "question2": {
        "text": "Which keyword is used to define a function in Python?",
        "options": ["func", "define", "def", "function"],
        "correct": 2
    },
    "question3": {
        "text": "How do you start a comment in Python?",
        "options": ["//", "#", "/*", "--"],
        "correct": 1
    },
    "question4": {
        "text": "Which of these is a mutable sequence type in Python?",
        "options": ["tuple", "list", "str", "int"],
        "correct": 1
    },
    "question5": {
        "text": "What is the output of print(type(5))?",
        "options": ["<class 'int'>", "int", "number", "<type 'int'>"],
        "correct": 0
    },
    "question6": {
        "text": "Which operator is used for exponentiation in Python?",
        "options": ["^", "**", "pow", "%"],
        "correct": 1
    },
    "question7": {
        "text": "How do you create a dictionary in Python?",
        "options": ["[1, 2, 3]", "{ 'a': 1, 'b': 2 }", "(1, 2)", "<1, 2>"],
        "correct": 1
    },
    "question8": {
        "text": "Which statement is used to handle exceptions?",
        "options": ["catch", "finally", "except", "error"],
        "correct": 2
    },
    "question9": {
        "text": "What is the result of len('Python')?",
        "options": ["5", "6", "7", "8"],
        "correct": 1
    },
    "question10": {
        "text": "How do you import the math module?",
        "options": ["import math", "include math", "using math", "require math"],
        "correct": 0
    },
    "question11": {
        "text": "Which function converts a string to an integer?",
        "options": ["str()", "int()", "float()", "bool()"],
        "correct": 1
    },
    "question12": {
        "text": "What is the output of print(3 * 'a')?",
        "options": ["aaa", "3a", "a3", "Error"],
        "correct": 0
    },
    "question13": {
        "text": "Which keyword is used to create a class in Python?",
        "options": ["struct", "class", "object", "type"],
        "correct": 1
    },
    "question14": {
        "text": "What does the range(5) function generate?",
        "options": ["0 to 5 inclusive", "1 to 5", "0 to 4", "1 to 4"],
        "correct": 2
    },
    "question15": {
        "text": "How do you add an item to the end of a list?",
        "options": ["list.add(item)", "list.append(item)", "list.insert(item)", "list.push(item)"],
        "correct": 1
    },
    "question16": {
        "text": "Which operator checks for equality?",
        "options": ["=", "==", "!=", "is"],
        "correct": 1
    },
    "question17": {
        "text": "What is the output of print('Hello'.upper())?",
        "options": ["hello", "HELLO", "Hello", "hELLO"],
        "correct": 1
    },
    "question18": {
        "text": "How do you start a for loop in Python?",
        "options": ["for i in range(5):", "for (i=0; i<5; i++):", "foreach i in range(5):", "loop i from 0 to 4:"],
        "correct": 0
    },
    "question19": {
        "text": "Which of these is a boolean value in Python?",
        "options": ["True", "Yes", "1", "OK"],
        "correct": 0
    },
    "question20": {
        "text": "What is the correct way to get user input?",
        "options": ["input()", "read()", "scan()", "get()"],
        "correct": 0
    }
}


''' Flow of program
 1. Start
 2. userName, score, questions
 3. Take name from user as input
 4. Welcome userName. Best of Luch for your quiz.
 5. Iterate through the questions and let the user answer
 6. If answer correct then increase the score else continue
 7. Continue iterating till the end of questions
 8. Show the score to user
 9. Stop
 
 Take Input from user -> user name

 '''
score = 0
count = 1
userName = ""
print("*"*13,"Hello! Welcome to the quiz Application","*"*13)
userName = input("Enter your name : ")


print(f"Welcome {userName} All the best for your quiz.")


# Iterating through questions
for que in questions:
    # Printing Questions
    print(count,questions[que]["text"])
    count +=1

    # print options
    options = questions[que]["options"]
    for i in range(len(options)):
        print("\t",i+1,options[i])

    answer = int(input("Enter the correct option No : "))
    correctIndex = questions[que]["correct"]
    if(answer-1==correctIndex):
        print("\tCorrect answer!")
        score+=1
    else:
        print("\tIncorrect!","the answer is",options[correctIndex])


print("*"*9,"Yayyy! quiz completed your score is ",score,"*"*9)