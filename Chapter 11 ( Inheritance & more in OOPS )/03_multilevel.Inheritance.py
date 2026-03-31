# 3) Multilevel Inheritance
# parent sa child 1 & then child 1 se child 2

class employee:
    a = 1

class programmer(employee):
    b = 2

class manager(programmer):
    c = 3

o = employee()
print(o.a) # Prints the attribute of a
# print(o.b) # Shows an error bcoz there is no b attribute in employee class


o = programmer()
print(o.a , o.b) # Prints the attribute of a & b

o = manager()
print(o.a , o.b , o.c) # Prints the attribute of a , b & c