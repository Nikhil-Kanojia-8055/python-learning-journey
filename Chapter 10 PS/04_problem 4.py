# Add a static method in problem 2 to greet a user hello 

class Calculator:
    def __init__(self , n):
        self.n = n

    def square(self): # For square 
        print(f"The square is : {self.n*self.n}")

    def cube(self):  # For cube
        print(f"The cube is : {self.n*self.n*self.n}")

    def squareroot(self):  # For squareroot
        print(f"The squareroot is : {self.n**1/2}")

    @staticmethod
    def hello():  # For greeeting/greet
        print("Hello world !")


a = Calculator(4)
a.hello()
a.square()
a.cube()
a.squareroot()