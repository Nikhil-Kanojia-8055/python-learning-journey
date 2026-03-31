# Create an class with a class attribute a; create an object from it & set 'a'
# directly using object.a = 0.Does this change the class attribute

class demo():
    a = 4

o = demo()
print(o.a) # prints the class attribute bcoz instance attribute is not present

o.a = 0 # instance attribute is set
print(o.a) # prints the class attribute bcoz instance attribute is present 

print(demo.a) # prints the class attribute

# Answer is no