class Employee:
    name = "Nikhil"
    langauge = "Python" 
    salary = 1200

Nikhil = Employee()
print(Nikhil.name , Nikhil.langauge)



class Employee:
    
    langauge = "Python" # This is an class attribute
    salary = 1200


Nikhil = Employee()
Nikhil.name = "Nikhil Kanojia" # This is an object attribute
print(Nikhil.name , Nikhil.langauge , Nikhil.salary)

Ram = Employee()
Ram.name = "Ram bhai"
print(Ram.name , Ram.salary , Ram.langauge)

# Here name is object attibute and salary and langauge are class attribute
# as they are directly belongs to an class