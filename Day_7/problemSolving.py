num1 = 899
target = 100000

# 17 + __ = 78

# 0 --> 78
for i in range(0,target):
    if i + num1 == target:
        print(i)
        break


print("This is the value we got from calculation : ",target - num1)
