age = 13
citizen = True

if age >=18:
    if citizen: 
        print("You're eligible to vote")
        print("Inside the nested if")
    else:
        print("Inside the nested else")
else:
    print("You're not allowed to vote")
    print("In the outside else block")