# keyword argumanets function
def total(*numbers):
    s = sum(numbers)
    return s


print(total(1,2,3,4,5,6,7,8,9))
print(total(1,2,3,4,5,6))
print(total(1,2,3,4))
print(total(1,2))