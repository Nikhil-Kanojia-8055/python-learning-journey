# Write a class train which has method to book ticket get status (no of tickets)
# and get info of train runnnning under indian railways..


from random import randint # Here from is an reserved keyword
class train():
    def __init__(self , TrainNo):
        self.TrainNo = TrainNo 

    def book(self , Fro , to):
        print(f"Ticket is booked in TrainNo {self.TrainNo} form{Fro} to {to}")

    def getstatus(self):
        print(f"Train No: {self.TrainNo} is running on time ")

                

    def getfare(self , Fro , to):
        print(f"Ticket Fare in TrainNo {self.TrainNo} form{Fro} to {to} is {randint(222,5555)}")


t = train(12345)
t.book("Rampur" , "Delhi")
t.getstatus()
t.getfare("Rampur" , "Delhi")