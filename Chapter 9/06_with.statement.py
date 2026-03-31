# f = open("file.txt")
# print(f.read())
# f.close()

# Now using this same code using the with statement :

with open("file.txt") as f:
    print(f.read())

# Here we have not to  use close() 