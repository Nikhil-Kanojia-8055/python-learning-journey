# Types of Inheritance -
# 1) Single Inheritance
# Base class se ek derived class ban gai

# 2) Multiple Inheritance
# more than 1 parent class 

class employee: # Base class / parent class
    company = "ITC"
    name = "Nikhil Kanojia"
    def show(self):
        print(f"The name of employee is {self.name} and the company is {self.company}")

class  coder:
    langauge = "Python"
    def printlangauges(self):
        print(f"Out of all langauges here is your langauges {self.langauge}")


class programmer(employee , coder): # Inherited class / Child class
    company = "ITC Infotech"
    def showlangauge(self):
        print(f"The name is {self.company} and he is good in {self.langauge} langauge")

a = employee()
b = programmer()
print(a.company , b.company)

b.show()
b.printlangauges()
b.showlangauge()

# NOTE : It is an way of creating a new class from a derived class

