from Item import Item

class DVD(Item):
    def __init__(self, name, borrowIn, borrowed=False, dateToReturn="", year=""):
        super().__init__(name, borrowIn, borrowed, dateToReturn)
        self.year = year
    
    def displayInfo(self):

        return f"(DVD) Name: {self.name}\nPrice: {self.price}\nBorrowed: {self.borrowed}\n"


