class Animal :
    def __init__(self, name, health , happiness, age):
        self.name = name
        self.health = health
        self.happiness = happiness
        self.age = age


    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Health: {self.health}")
        print(f"Happiness: {self.happiness}")
        print(f"Age: {self.age}")
        return self
    

    def feed(self, happiness, health):
        self.happiness += happiness
        self.health += health
        return self