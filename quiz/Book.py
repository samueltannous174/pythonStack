from Item import Item

class Book(Item):
    def __init__(self, name, borrowIn, borrowed=False ,author=""):
        super().__init__(name, borrowIn, borrowed)
        self.author = author
    
    def displayInfo(self):
        print(f"Book Name: {self.name}")
        print(f"Price: {self.price}")
        print(f"Borrowed: {self.borrowed}")
        return self
    