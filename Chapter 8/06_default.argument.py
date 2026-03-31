def Goodday(name,ending = "hello"):
    print("Goodday",name)
    print(ending)
    return "ok"
# here name and ending are the argument which is called when the function is called

a = Goodday("Nikhil","Thanku")
print(a)
# here the argument is already given

# return is used here for ek value leke ja aaur jo mange usko dedena
b = Goodday("Ram")
print(b)
# here the argument is not given so it will take hello as default argument


