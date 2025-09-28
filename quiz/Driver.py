from Item import Item
from Book import Book
from Dvd import DVD
from Magazine import Magazine


array=[]

array.append(Book("book1", 2))
array.append(DVD("dvd1", 3 ))
array.append(Magazine("magazine2", 4))

def display(item):
    print(item.displayInfo())
    print("------------------------")

display(array[1])
display(array[0])
display(array[2])


