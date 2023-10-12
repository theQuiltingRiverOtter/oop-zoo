from animal import Animal


class Mammal(Animal):
    def __init__(self, name: str, species: str):
        super().__init__(name, species)

    def give_birth(self):
        return f"{self.name} the {self.species} has given birth"

    def speak(self):
        return "Mammal sound"
