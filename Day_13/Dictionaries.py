# Syntax
# dictionary_name = {
#  key1: value1,
#  key2: value2
# }

# Example of creating a dictonary
student = {
    "name" : "Ayush",
    "class" : 4,
    "rollNo" : 9,
    "subjects" : {"Maths","Science","Marathi"},
    "isStudentPass"  :True,
    'hobbies' : ["Singing","Cycling"],
    "age" : 10
}
print(type(student))
print(student)

# Dictonary using dict function
emp = dict(name="Sai",company="Google",role="SDE")
print(type(emp))
print(emp)


# accesing data 
print("Student name : ",student["name"])

# accesing data using get 
print("Student name : ",student.get("LAstname"))


# adding a value into student
print("Before :",student)

student["school"] = "NHSL"

print("After :",student)


# updating dictonary values
animal = {
    "name" : "Dog",
    "colour" : "Black"
}

print(animal)
animal["colour"] = "Brown"
print(animal)

# removing dictonary values
animal = {
    "name" : "Dog",
    "colour" : "Black",
    "breed" : "German Shepard",
    "owner"  :"no"
}
print(animal)
animal.pop("breed")
print(animal)


print(animal)
del animal["breed"]
print(animal)


animal = {
    "name" : "Dog",
    "colour" : "Black",
    "breed" : "German Shepard",
    "owner"  :"no"
}
print(animal)
animal.clear()
print(animal)

# methods of dictonary
student = {
 "name": "Rahul",
 "marks": 85
}
print(student.keys())
print(student.values())
print(student.items())

# traversing through dictonary
student = {
 "name": "Rahul",
 "marks": 85
}

for key in student:
    print(student.get(key))


# traversing values
for value in student.values():
    print(value)

# traversing keys
for key in student.keys():
    print(key)

# traversing through items
# dict_items([('name', 'Rahul'), ('marks', 85)]) 
for key,value in student.items():
    print(key , " : ",value)


# Nested Dictonaries
students = {
    "student1" : {
        "name" : "Omkar",
        "rollNo" : 45
    },
    'student2':{
        "name" : "Ram",
        "rollNo" : 76
    }
}

print(students["student1"]["name"])