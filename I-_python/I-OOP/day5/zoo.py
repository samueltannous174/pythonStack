

from lion import Lion
from tiger import Tiger


class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name
    def add_lion(self, power, name, health, happiness, age ):
        lion = Lion(power, name, health, happiness, age)
        self.animals.append(lion)
        return lion
    def add_tiger(self, name):
        self.animals.append( Tiger(name) )
        return self
    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()
            
zoo1 = Zoo("John's Zoo")
lion= zoo1.add_lion(10,"Nala", 0, 0, 5)
lion.feed()
print(lion.health)
