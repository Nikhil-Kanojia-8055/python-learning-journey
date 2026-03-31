# WAP for using function to find greatest among 3 numbers

def greatest(a,b,c):
    if(a>b and a>c):
     return a
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c

# a= int(input("number"))
# b= int(input("number"))
# c= int(input("number"))
a = 21
b = 5
c = 665
print(greatest(a,b,c))

