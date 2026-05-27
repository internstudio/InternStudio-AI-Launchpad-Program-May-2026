# Parameters --> The values decalred in defincation of funciton
# declaration of parametarized function
def add(num1, num2, isUserVerified):
    addition = num1 + num2
    print(isUserVerified)
    print("Addition is : ",addition)

# calling funciton
# Arguments --> the values passed while calling function
# add(1,2,True)
# add(3,4,True)
# add(5,2,True)
# add(6,2,True)


# declaration of parametarized function with default values
def add1(num1=45, num2=67, isUserVerified = False):
    addition = num1 + num2
    print(isUserVerified)
    print("Addition is : ",addition)

# calling funciton
# add1()
# add1()


# calling with keyword arguments
add(isUserVerified=True,num1=23,num2=35)