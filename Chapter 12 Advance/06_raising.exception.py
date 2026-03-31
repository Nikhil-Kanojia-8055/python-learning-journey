a = int(input("Enter 1st number :"))
b = int(input("Enter 2nd number :"))

if(b == 0):
    raise ZeroDivisionError("Hey our program is not ment to divide numbers by zero")
# It is used to show the error & crash the code 
else:
    print(f"The division of a/b is{a/b}")