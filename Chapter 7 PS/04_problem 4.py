# WAP for number is prime or not which is comingin table itself

n = int(input("Enter a number : "))

for i in range(2,n):
   if(n%i) == 0:
    print("number is not prime")
    break

else:
    print("number is prime")
