class Employee:
    
    langauge = "Python" # This is an class attribute
    salary = 1200

    def getinfo(self):
        print(f"The langauge is {self.langauge} . The salary is {self.salary}")
    def greet(self):
        print("Good Morning")

Nikhil = Employee()
Nikhil.langauge = "Java" # This is an object attribute

Nikhil.greet()

Nikhil.getinfo()
# Employee.getinfo(Nikhil)