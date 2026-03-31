# Create a class 'programmer' for storing information of few programmer working in Microsoft

class programmer:
    company = "Microsoft"
    def __init__(self , name , salary , pin):
        self.name = name
        self.salary = salary
        self.pin = pin

p = programmer("Harry" , 120000 , 34867)
print(p.name , p.salary , p.pin , p.company)

r = programmer("Rohan" , 500000 , 328902)
print(r.name , r.salary , r.pin , r.company)