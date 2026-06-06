name = "Ram"
lastName = 'Patel'

paragraph = """This is the paragraph that contains information about the person.
In this section we'll cover about the skills he have"""

print(name)
print(name)
print(paragraph)


# accesing characters in string
str1 = "Elen"
print(str1[1])
print(str1[2])
print(str1[3])
print(str1[-1])

# String Slicing
# syntax
# string_name[start:end]
str1 = "Python Programming"
# Python
print(str1[0:6])
print(str1[:6])

# Programming
print(str1[7:18])
print(str1[7:])


# using step value
str2 = "0123456789"
# syntax
# stringName[start:end:step]
print(str2[::2])


# Reversing
str3 = "Reversing in python"
print(str3[::-1])


# Finding length
str3 = "Reversing in python"
print(len(str3))

# String Concatination
firstName = "Sai"
lastName = "Bhosale"

fullName = firstName + " " + lastName
print(fullName)


# string repetation
print("Python Program!" * 10)

# Membership operations
str3 = "Reversing in Python"
print("Python" in str3)
print("Java" not in str3)

# String method
str1  = "sachin Tendulkar"
print(str1.lower())
print(str1.upper())
print(str1.title())
print(str1.capitalize())


# removing space from string
str1 = "   This is the string    " + "shaj;lkjfd"
print(str1)
print(str1.strip())
print(str1.lstrip())
print(str1.rstrip())

# find 
str1  = "sachin Tendulkar chin chin"
print(str1.find("uio"))

print(str1.index("uio"))

# counting occurances
str1 = "Banananaa"
print(str1.count("na"))


#  Replacing Text
# replace()
text = "I like Java"
new_text = text.replace("Java", "Python")
print(new_text)

# split
studentName = "Sai Shankar Ram Sham Ramesh Ganesh Mahesh"
print(studentName.split())


studentName1 = "Sai,Shankar, Ram, Sham, Ramesh, Ganesh, Mahesh"
print(studentName1.split(","))


# join()
# Combines list elements into a string.
languages = ["Python", "Java", "C++"]
result = ", ".join(languages)
print(result)

# checking string validation
# isalpha()
# Checks if all characters are alphabets.
name = "Python"
print(name.isalpha())


# isdigit()
# Checks if all characters are digits.
num = "ajdfs;lk"
print(num.isdigit())

# isalnum()
# Checks if string contains letters and numbers only.
text = "Python123"
print(text.isalnum())

# isupper()
text = "PYTHON"
print(text.isupper())

# islower()
text = "python"
print(text.islower())

# string formatting
name = "John"
age = 25
print("My name is {} and I am {} \"  years old".format(name, age))


name = "John"
age = 25
print(f"My name is {name} and \n I am {age} years \t  old")