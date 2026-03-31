a = int(input("Enter your age : "))
# we are giving int in input because we want an iteger value otherwise
# it will take input as string


# imultiple if statement

# if satatement 1:
if(a%2 == 0):
    print("Number is even")
# end of 1 statement

# if satatement 2:
if(a>=18):
    print("You are above the age")
    print("Good luck")
    # the space infront of print function is indentation which means that
    # you are in the if function
# end of 2 statement


elif(a<0):
    print("You are entering an invalid age")

elif(a==0):
    print("You are entering 0")

else:
    print("You are below the age ")
    print("Sorry")

print("Endof program")


# if akela ho sakta hai but else,elif akela nhi ho sakta