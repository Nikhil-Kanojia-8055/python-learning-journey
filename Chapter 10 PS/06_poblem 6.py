# Can u change the self-parameter inside a class to something else ("Say Nikhil")
# try changing Self to 'slf' or 'nikhil' & see the effects


from random import randint # Here from is an reserved keyword
class train():
    def __init__(slf , TrainNo): # 1) We have change self to slf but no changess occurs
        slf.TrainNo = TrainNo 

    def book(Nikhil , Fro , to): # 2) 1) We have change self to Nikhil but no changess occurs
        print(f"Ticket is booked in TrainNo {Nikhil.TrainNo} form {Fro} to {to}")

    def getstatus(self):
        print(f"Train No: {self.TrainNo} is running on time ")

    def getfare(self , Fro , to):
        print(f"Ticket Fare in TrainNo {self.TrainNo} form{Fro} to {to} is {randint(222,5555)}")


t = train(12345)
t.book("Rampur" , "Delhi")
t.getstatus()
t.getfare("Rampur" , "Delhi")

# NOTE : Nothing happens due to changing it just it will make code complex and readablity of code will destroy