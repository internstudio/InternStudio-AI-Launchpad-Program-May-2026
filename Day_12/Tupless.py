# Syntax for tuple
# tuple_name = (item1, item2, item3)

tp1= ("Apple","Banana","Mango","Orange")
print(tp1[1])

tp1[0] = "Grapes"


# single element tuple
tp2 = (12,)
print(type(tp2))


# tuple slicing
numbers = (10, 20, 30, 40, 50)
print(numbers[1:4])


# tuple concatination
t1 = (1, 2)
t2 = (3, 4)
print(t1 + t2)

# Repetation
t1 = (1, 2)
print(t1*4)

# membership operator in tuple
t1 = (1, 2,"Cog")
print("Cog" in t1)

# Inbuilt functions
numbers = (10, 20, 10, 30)
print("Sum",sum(numbers))
print("Min",min(numbers))
print("Max",max(numbers))

# Inbuilt methods
print("Count",numbers.count(100))
print("Index",numbers.index(20))