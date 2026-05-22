# Logical Operators Example

age = 7
has_id = False
is_banned = False

# AND operator
if age>=18 and has_id:
    print('You re allowed')
else:
    print("not allowed")

# 1st | 2nd | Result
# True | True | True
# False | True | False
# True | False | False
# False | False | False

# OR operator
age = 7
has_id = True
if age <= 18 or not has_id:
    print("You cannot access restricted area.")
else:
    print("Access granted.")

# 1st | 2nd | Result
# True | True | True
# False | True | True
# True | False | True
# False | False | False


# NOT operator
if not is_banned:
    print("User account is active.")
else:
    print("User account is banned.")
# True --> False
# False --> True