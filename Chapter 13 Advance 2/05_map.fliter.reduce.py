# Map example
from functools import reduce
l = [435,5,34,52,54,534,5,5,5,234,53,51,5,35,77]
squared = list(map(lambda x: x *x,l))
print(squared)

# Filter example
def even(n):
    if(n%2==0):
        return True
    return False
only_even =list(filter(even,l))
print(only_even)

# Reduce example
def sum(a,b):
    return a+b
mul = lambda a,b:a*b
print(reduce(sum,l))  # it will take first two element and apply sum function then take the result and next element and so on...
print(reduce(mul,l))  # it will take first two element and apply mul function then take the result and next element and so on...