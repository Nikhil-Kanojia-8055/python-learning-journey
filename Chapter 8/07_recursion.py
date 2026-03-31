# Recursion is a function which call itself
''' 
Factorial(0) = 1
Factorial(1) = 1
Factorial(2) = 2 * 1
Factorial(3) = 3 * 2 * 1

Factorial (n) = n * Factorial(n-1)

'''
def Factorial(n):
    if(n == 1 or n == 0):
        return 1
    return n * Factorial (n-1)

n = int(input("Enter your number :"))
print(f"The factorial of this number is :{Factorial(n)}")
