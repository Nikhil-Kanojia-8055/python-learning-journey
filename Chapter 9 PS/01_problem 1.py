# WAP to read text from a given poem.txt and find out wheather it contains a word "twinkle" or not

f = open("poem.txt")
content = f.read()

if("Twinkle" in content):
    print("The word Twinkle is present in the poem")

else:
    print("The word Twinkle is not present in the poem")
    
f.close()