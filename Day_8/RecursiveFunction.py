def countdown(n): 
#  base condition
    if n == 0: 
        return 
 
    print(n) 
 
#  recursion
    countdown(n - 1) 
 
countdown(5) 

# n = 5 == 0 --> False --> print --> countdown(n-1=4)
# n = 4 == 0 --> False --> print --> countdown(n-1=3)
# n = 3 == 0 --> False --> print --> countdown(n-1=2)
# n = 2 == 0 --> False --> print --> countdown(n-1=1)
# n = 1 == 0 --> False --> print --> countdown(n-1=0)