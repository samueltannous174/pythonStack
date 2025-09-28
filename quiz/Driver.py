from Item import Item
from Book import Book
from Dvd import DVD
from Magazine import Magazine
from User import User

items=[]

user = User("samuel", "sam@gmail.com", 22)


items.append(Book("book1", 2))
items.append(DVD("dvd1", 3 ))
items.append(Magazine("magazine2", 4))

def display(item):
    print(item.displayInfo()) # displayInfo overriding
    print("------------------------")

display(items[1])
display(items[0])
display(items[2])



user.addItem(items[0])
user.addItem(items[1])
user.addItem(items[2])

user.displayArray()
