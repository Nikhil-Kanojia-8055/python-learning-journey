try:
    a = int(input("Hey! ,Enter a number :"))
    print(a) # If we will write this much code only and if user give the input as string so the code will crash
except Exception as e:
    print(e)

print("Thnak you")