from animal import Animal


class Reptile(Animal):
    def __init__(self, name: str, species: str):
        super().__init__(name, species)

    def bask_in_sun(self):
        return f"{self.name} the {self.species} is basking in the sun"

    def speak(self):
        return "hiss hiss"
