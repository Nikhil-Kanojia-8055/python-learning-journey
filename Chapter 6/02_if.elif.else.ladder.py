a = int(input("Enter your age : "))
# we are giving int in input because we want an iteger value otherwise
# it will take input as string


# if elif else ladder

if(a>=18):
    print("You are above the age")
    print("Good luck")
    # the space infront of print function is indentation which means that
    # you are in the if function

elif(a<0):
    print("You are entering an invalid age")

elif(a==0):
    print("You are entering 0")

else:
    print("You are below the age ")
    print("Sorry")

print("Endof program")