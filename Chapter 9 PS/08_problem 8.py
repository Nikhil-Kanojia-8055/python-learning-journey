# WAP to make copy of text file "This.txt"

with open("This.txt") as f:
    content = f.read()
with open("This_copy.txt" , "w") as f:
    content = f.write(content)