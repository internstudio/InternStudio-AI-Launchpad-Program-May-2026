print(1)
print(2)
print(3)
print(4)
print(5)
print(6)
print(7)
print(8)
print(9)
print(10)

# for variable in sequence: 
#     statements

for i in range(1,6):
     print("The current number is : ",i)

# n = 6 n-1
# i --> 1
# i --> 2
# .
# .
# .
# i --> 6




num = 79
target = 734

for i in range(1,1000):
    newNum = num + i
    if newNum == target:
        print(i)