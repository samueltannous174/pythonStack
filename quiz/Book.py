from Item import Item

class Book(Item):
    def __init__(self, name, borrowIn, borrowed=False ,author=""):
        super().__init__(name, borrowIn, borrowed)
        self.author = author
    
    def displayInfo(self):
        return f"(Book) Name: {self.name}\nPrice: {self.price}\nBorrowed: {self.borrowed}\n"