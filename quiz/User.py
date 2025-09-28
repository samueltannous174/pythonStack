class User:
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.borrowArray=[]


    def addItem(self, item):
        self.borrowArray.append(item)   

    def displayArray(self): 
        print("*******************************************************************************")
        for item in self.borrowArray:
            print("------------------------")
            print(item.displayInfo())
            