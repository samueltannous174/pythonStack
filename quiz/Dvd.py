from Item import Item

class DVD(Item):
    def __init__(self, name, borrowIn, borrowed=False, dateToReturn="", year=""):
        super().__init__(name, borrowIn, borrowed, dateToReturn)
        self.year = year
    
    def displayInfo(self):
        print(f"DVD Name: {self.name}")
        print(f"Price: {self.price}")
        print(f"Borrowed: {self.borrowed}")
        return self
    

