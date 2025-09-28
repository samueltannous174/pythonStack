from Item import Item

class Magazine(Item):
    def __init__(self, name, borrowIn, borrowed=False , author="", cover=""):
        super().__init__(name, borrowIn, borrowed)
        self.cover = cover

    def displayInfo(self):
        return f"(Magazine) Name: {self.name}\nPrice: {self.price}\nBorrowed: {self.borrowed}\n"
