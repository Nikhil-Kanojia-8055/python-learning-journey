# WAP for converting celcius to fehrenhite using function
# formulae 5*(f-32)/9

def f_to_c(f):
    return 5*(f-32)/9

f = int(input("Enter temp in f :"))
print(f_to_c(f))

# using of round function in python

def f_to_c(f):
    return 5*(f-32)/9

f = int(input("Enter temp in f :"))
c = f_to_c(f)
print(f"{round (c,2)} in celcius")