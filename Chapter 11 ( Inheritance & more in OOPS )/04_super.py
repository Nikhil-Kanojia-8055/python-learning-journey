class employee:
    def __init__(self):
        print("The Constructor of employee ")
    a = 1

class programmer(employee):
    def __init__(self):
        print("The Constructor of programmer ")
    b = 2

class manager(programmer):
    def __init__(self):

        super().__init__() # It will run its parent constructor (programmer) also this is use of an super keyword
        
        print("The Constructor of manager ")
    c = 3

# o = employee()
# print(o.a) # Prints the attribute of a

# o = programmer()
# print(o.a , o.b) # Prints the attribute of a & b

o = manager()
print(o.a , o.b , o.c) # Prints the attribute of a , b & c