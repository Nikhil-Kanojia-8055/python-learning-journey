# create an empty dictonary allow 4 friends to enter there fav langauge
# as value and keys asthere names assume that all names are unique

# problem 6 # if the names of 2 friends are same what will happen to program in problem 6

# in it the values can be same but the key cnnot be same because if there are 2 friends same name
# then it will update the new value what is coming next 

d = {}
name = input("Entr your name : ")
lang = input("Enter langauge name : ")
d.update({name:lang})

name = input("Entr your name : ")
lang = input("Enter langauge name : ")
d.update({name:lang})

name = input("Entr your name : ")
lang = input("Enter langauge name : ")
d.update({name:lang})

name = input("Entr your name : ")
lang = input("Enter langauge name : ")
d.update({name:lang})

print(d)