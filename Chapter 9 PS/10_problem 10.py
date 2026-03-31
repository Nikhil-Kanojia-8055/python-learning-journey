# WAP to wipe out the content of a file using python

with open("wipe.txt" , "w") as f:
    content = f.write("")

'''
By doing this :
content = f.write("")
whole content of the file will wipe out
'''