# Syntax for lists
# list_name = [item1, item2, item3]

# Example with list and without lists
rollNo1 = 23
rollNo2 = 25
rollNo3 = 24

rollNos = [23,25,24]


animals = ["Cat","Dog","Cow"]
# print(animals)

objects = [2,True,2.23,"InternStudio"]

empNo = 123456
empName = "John Doe"
empDept = "R&D"
empSalary = 80000.80
empLocation = "Pune"
empVerified = True


# Creating lists with diff data types
empInfo = [12345,"John Doe","R&D",80000.90,"Pune",True]

for el in empInfo:
    print(el)


# List of Numbers
numbers = [10, 20, 30, 40]
# List of Strings
names = ["Aman", "Rahul", "Priya"]

fruits = ["Apple", "Banana", "Mango","Coconut"]
# Normal/Positive Indexing
#           0         1         2        3
#           -4        -3      -2         -1                          

print(fruits[-1])
print(fruits[0])
print(fruits[3])

numbers = [10, 20, 30, 40, 50]
print(numbers[1])
print(numbers[2])
print(numbers[3])


numbers = [10, 20, 30, 40, 50]

# slicing in the list
# start index  = 1
# 4 = 4-1 = 3
print(numbers[1:4])






fruits = ["Apple", "Banana", "Mango","Coconut"]
# Modifying a list
print("Before Modificaiton : ",fruits)
fruits[1] = "Papaya"
print("After Modificaiton : ",fruits)

# appending an element
fruits = ["Apple", "Banana", "Mango","Coconut"]
print("Before Appending : ",fruits)
fruits.append("Orange")
fruits.append("Banana")
fruits.append("Grapes")
print("After Appending",fruits)


# Insert 
fruits = ["Apple", "Banana", "Mango","Coconut"]
print("Before : ",fruits)
fruits.insert(1,"Orange")
print("After : ",fruits)

# Extend 
fruits = ["Apple", "Banana", "Mango","Coconut"]
print("Before : ",fruits)
fruits.extend(["Grapes","Papaya","Watermelon","Pineapple"])
print("After : ",fruits)

# removing an element 
fruits = ["Apple", "Banana", "Mango","Coconut"]
print("Before : ",fruits)
fruits.remove("Apple")
print("After : ",fruits)

# Pop
fruits = ["Apple", "Banana", "Mango","Coconut"]
print("Before : ",fruits)
fruits.pop(1)
print("After : ",fruits)


# clear
fruits = ["Apple", "Banana", "Mango","Coconut"]
print("Before : ",fruits)
fruits.clear()
print("After : ",fruits)


# list operations

numbers1 = [1,2,3,4,5,6]
numbers2 = [7,8,9,10]

combined = numbers1+numbers2
# print(combined)


# print(numbers1*10)

# checking existance of element
print(47 in numbers1)


# functions of list
numbers = [10, 5, 25, 15]
print("Length is : ",len(numbers))
print("Minimum : ",min(numbers))
print("Maximum : ",max(numbers))
print("Sum : ",sum(numbers))

# Iterating through loop 1st way
numbers = [10, 5, 25, 15]
for num in numbers:
    print(num)

# 2nd way
numbers = [10, 5, 25, 15]
for i in range(0,len(numbers)):
    print(numbers[i])

students = [
 ["Rahul", 85],
 ["Priya", 90],
 ["Amit", 78]
]

print(students[2][1])