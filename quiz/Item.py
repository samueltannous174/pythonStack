import datetime

class Item:
    def __init__(self, name, price, borrowed=False , dateToReturn=""):
        self.name = name
        self.price   = price
        self.borrowed = borrowed
        self.dateToReturn = dateToReturn

    def displayInfo(self):
     
        return f"Item Name: {self.name}\nPrice: {self.price}\nBorrowed: {self.borrowed}\n"
    
    def borrow(self):
        self.borrowed = True
        
    def returnItem(self):
        self.borrowed = False

    def checkIfBorrowed(self):
        if self.borrowed == True:
            print("Item is borrowed")
        else:
            print("Item is not borrowed")
        return self.borrowed
        
    def calculateLateFee(self):
        today = datetime.datetime.now()
        days_overdue =  today - self.dateToReturn
        if days_overdue > 0:
            return days_overdue * 0.1
        else:
            return 0