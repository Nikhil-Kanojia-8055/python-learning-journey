dict = {
    
    "Nikhil" : 80,
    "bhai 1" : 20,
    "bhai 2" : 78,
    "bhai 3" : 10,

    }   
print(dict.items())
# it gives us dictonary in theform of tuples

print(dict.keys())
# it will return the key or index of the names

print(dict.values())
#  here it will print the vaues presented in the dict

dict.update({"Nikhil":88,"bhai 4":8})
print(dict)
# used for the updating purpose proof of mutablity
# also use for adding somthing

print(dict.get("Nikhil"))
print(dict.get("Ram"))
# it tell that the key is presented in the list or not


# dict 2 = {}
# empty dictonary
