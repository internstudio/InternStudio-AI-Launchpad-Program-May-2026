# Pattern 2 
# 54321 
# 5432 
# 543 
# 54 
# 5 

n = 6

for i in range(1,n+1):
    for j in range(n,i-1,-1):
        print("*",end="")
    print()
# i  =5 = j = 5 5 -> 4 -> 3 -> 2 -> 1


# ******
# *****
# ****
# ***
# **
# *


10