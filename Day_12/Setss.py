# syntax 
# set_name = {item1, item2, item3}

s1 = {1,1,11,2,34,5,6,7,7,8,9}
print(type(s1))
print(s1)

# creating an empty set
s2 = set()
print(type(s2))

# Set of Numbers
numbers = {10, 20, 30}

# Set of Strings

# Set with mutliple data types
names = {"Rahul", "Amit", "Priya",}
print(names)

# add number to set
names = {"Rahul", "Amit", "Priya",}
print("Before :",names)
names.add("Shiv")
print("After :",names)

# udpate method in set
names = {"Rahul", "Amit", "Priya",}
print("Before :",names)
names.update(["Shiv","Sai","Ankit"])
print("After :",names)



numbers = {1,2,3,4,5,6,12}
# remove()
numbers.remove(20)

# Produces error if value doesn't exist.
# discard()
numbers.discard(20)

# No error if value doesn't exist.
# pop()
# Removes random element.
numbers.pop()

# clear()
# Removes all elements.
numbers.clear()


# Membership Operators
num1 = {1,23,4,5}
print(5 in num1)

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Union
print(A.union(B))
print(A | B)

# Union
# Combines all elements.
print(A | B)


# Intersection
# Common elements.
print(A & B)


# Difference
# Elements present in first set only.
print(A - B)


# Symmetric Difference
# Elements present in either set but not both.
print(A ^ B)

numbers = {1,2,2,3,4,5}
for i in numbers:
    print(i)