# Create a class employee & add salary & increment properties to it

class empolyee:
    salary = 2345
    increment = 20
    @property
    def salaryafterincerement(self):
        return(self.salary + self.salary * (self.increment/100))

    @salaryafterincerement.setter
    def salaryafterincerement(self , salary):
        self.incerment = ((salary/self.salary)-1) *100 

e = empolyee()
print(e.salaryafterincerement)
e.salaryafterincerement = 2345
print(e.increment)

