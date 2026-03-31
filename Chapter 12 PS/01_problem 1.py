# WAP to open 3 files 1.txt , 2.txt , 3.txt if any of these files are not present a msg without exsisting the program must be printed promoting the same
try:
    with open("1.txt" , "r") as f:
        print(f.read())
except Exception as e:
    print(e)

try:
    with open("2.txt" , "r") as f:
        print(f.read())
except Exception as e:
    print(e)

try:
    with open("3.txt" , "r") as f:
        print(f.read())
except Exception as e:
    print(e)

print("Thank you")