# Create a class pets from a class animals & future create a class dog from pets add a method bark to class dog

class animals:
    pass

class pets(animals):
    pass

class dog:
    @staticmethod
    def bark():
        print("Bow Bow !!")

d = dog()
d.bark()
    