class Employee:
    
    langauge = "Python" # This is an class attribute
    salary = 1200

    def _init_(self): # Dunder method which is called automatically
        print("I am creating an object")

    def getinfo(self):
        print(f"The langauge is {self.langauge} . The salary is {self.salary}")
    
    @staticmethod
    def greet():
        print("Good Morning")

Nikhil = Employee()
Nikhil.name = "Nikhil Kanojia"
print(Nikhil.name , Nikhil.langauge)
Nikhil.greet()
Nikhil._init_()


