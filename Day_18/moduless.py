# syntax 
#1. import module_name
# program -> math -> fun
import math
print(math.sqrt(25))

# 2. import module_name as m
import math as m
print(m.sqrt(25))

# 3. from module_name import functionality
from math import sqrt
print(sqrt(25))

# 4. from module_name import f1,f2,f3
from math import sqrt,factorial,ceil
print(sqrt(35))
print(factorial(76))
print(ceil(8.45))

# 5. from module_name import *
# program -> fun
from math import *
print(sqrt(76))