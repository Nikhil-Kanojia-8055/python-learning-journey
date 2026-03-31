f = open("file.txt")

lines = f.readlines()
# It wil read the lines in the formate of list and the type will also return as an list

print(lines,type(lines))
# It will return the type as list and also the lines presented in the file in the formate of list

f.close()


# Next function


f = open("file.txt")

# lines = f.readlines()
# It wil read the lines in the formate of list and the type will also return as an list

# print(lines,type(lines))
# It will return the type as list and also the lines presented in the file in the formate of list

line1 = f.readline()
print(line1 , type(line1))
# print the string of line 1

line2 = f.readline()
print(line2 , type(line2))
# print the string of line 2

line3 = f.readline()
print(line3 , type(line3))
# print the string of line 3

line4 = f.readline()
print(line4 , type(line4))
# print the string of line 4

line5 = f.readline()
print(line5 , type(line5))
# print the string of line 5

line6 = f.readline()
print(line6 , type(line6))
# print the string of line 6

line7 = f.readline()
print(line7 == "")
# print the string of line 7 which is not here so it will print an empty string

f.close()