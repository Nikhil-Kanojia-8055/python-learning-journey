class Employee:
    
    langauge = "Python" # This is an class attribute
    salary = 1200

#1)
Nikhil = Employee()
Nikhil.langauge = "Java" # This is an object attribute
print( Nikhil.langauge , Nikhil.salary)
#2)
Nikhil = Employee()
#Nikhil.langauge = "Java" # This is an object attribute
print( Nikhil.langauge , Nikhil.salary)
# Instance attribute jo hai vo prefrence leta hai