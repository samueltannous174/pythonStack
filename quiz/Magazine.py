from Item import Item

class Magazine(Item):
    def __init__(self, name, borrowIn, borrowed=False , author="", cover=""):
        super().__init__(name, borrowIn, borrowed)
        self.cover = cover
