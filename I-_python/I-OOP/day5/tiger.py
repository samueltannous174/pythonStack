from animal import Animal
class Tiger (Animal):
    def __init__(self, color = "orange", name="Tiger", health = 0, happiness = 0, age = 5  ):
        self.color = color
        super().__init__("Tiger", 0, 0, 5)
    

    def feed(self):
        if self.color == "orange":
            happinessIncrease = 10
            healthIncrease = 10
        else:
            happinessIncrease = 5
            healthIncrease = 5

        return super().feed(happinessIncrease, healthIncrease).display_info()
    