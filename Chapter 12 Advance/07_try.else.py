try:
    a = int(input("Hey! ,Enter a number :"))
    print(a) # If we will write this much code only and if user give the input as string so the code will crash

# In  try else if the try part is runned successfully then only the else part will run

except Exception as e:
    print(e)

# If try part is runned sucessfully then only this will
else:
    print("I am inside else block")
