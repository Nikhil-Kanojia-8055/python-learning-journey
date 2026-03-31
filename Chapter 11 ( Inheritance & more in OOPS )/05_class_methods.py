class employee:
    a = 1

    @classmethod
    def show(cls): # if not then 23 will print
        print(f"The class attribute of a is {cls.a}")

e = employee()
e.a = 23

e.show()