class employee: # Base class / parent class
    company = "ITC"
    def show(self):
        print(f"The name of employee is {self.name} and the salary is {self.salary}")


class programmer(employee): # Inherited class / Child class
    company = "ITC Infotech"
    def showlangauge(self):
        print(f"The name is {self.name} and he is good in {self.langauge} langauge")

a = employee()
b = programmer()
print(a.company , b.company)

# NOTE : It is an way of creating a new class from a derived class
