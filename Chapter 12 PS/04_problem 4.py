# WAP to display a/b where a & b are 2 integers . if b==0,display infinite by handeling the 'ZeroDivisionError'

try:
    a = int(input("enter a number"))
 b = int(input("enter a number")) 
     print(a/b)
except ZeroDivisionError as v:
    print("infinite:")

    # ERROR