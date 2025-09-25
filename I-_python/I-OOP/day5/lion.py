from animal import Animal

class Lion(Animal):
    def __init__(self, power = 5, name="Lion", health = 0, happiness = 0, age = 5):
        self.power = power
        super().__init__(name, health, happiness, age)


    def feed(self):
        print( self.power)
        if self.power >= 5:
            healthIncrease=50;
            happinessIncrease=50
        else:
            healthIncrease=5
            happinessIncrease=5
    
        return super().feed(happinessIncrease, healthIncrease).display_info()