# A file contain a word 'Donkey' multiple times.You need to write aa code to replace a word ##### by updating same file

word = "Donkey"

with open("file.txt" , "r") as f:
    content = f.read()

contentNew = content.replace(word , "#####")
with open("file.txt" ,  "w") as f:
    f.write(contentNew)