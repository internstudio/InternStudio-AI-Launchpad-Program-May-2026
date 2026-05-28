age = 22 
citizen = False
 
if age >= 18: 
    
    print("Passed 1/2 : Person age is greater than 18")
    if citizen: 
        print("Passed 2/2 : Person is citizen of country")
        print("Eligible to Vote") 
    else:
        print("Failed 2/2 : person is not citizen of country")
else:
    print("Failed 1/2 Person age is less than 18 ")