# WAP to find out whether a file is identical & matches the content of another file

with open("This.txt") as f:
    content1 = f.read()
with open("This_copy.txt") as f:
    content2 = f.read()

if(content1 == content2):
    print("Yes these files are identical same")

else:
    print("No these files are not identical same")

# for same files

with open("This.txt") as f:
    content1 = f.read()
with open("log.txt") as f:
    content2 = f.read()

if(content1 == content2):
    print("Yes these files are identical same")

else:
    print("No these files are not identical same")

# Not same
