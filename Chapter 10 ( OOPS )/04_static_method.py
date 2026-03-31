class Employee:
    
    langauge = "Python" # This is an class attribute
    salary = 1200

    def getinfo(self):
        print(f"The langauge is {self.langauge} . The salary is {self.salary}")
    @staticmethod
    def greet():
        print("Good Morning")

Nikhil = Employee()

Nikhil.greet()

Nikhil.getinfo()
