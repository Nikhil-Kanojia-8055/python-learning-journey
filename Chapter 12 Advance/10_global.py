a = 43 # Global variable run outside the function & outside the function
def fun():
    a = 3 # Local variable run inside the function
    print(a)
fun()
print(a)