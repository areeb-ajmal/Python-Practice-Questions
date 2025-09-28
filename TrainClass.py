from random import randint

class Train :
    def __init__(self, train_no, fro, to):
        self.train_no = train_no
        self.fro = fro
        self.to = to

    def getbooked(self):
        print(f"Train no : {self.train_no} is booked {self.fro} to {self.to}")

    def getStatus(self):
        print(f"Train no : {self.train_no} is running on time")

    def getfare(self):
        print(F"Fare for Train no : {self.train_no} from {self.fro} to {self.to} is PKR {randint(222, 555)}")



p1 = Train(22314, "Alipur", "Bhawalpur")
p1.getbooked()
p1.getStatus()
p1.getfare()
        
        
        