from mammal import Mammal


class Marsupial(Mammal):
    def __init__(self, name: str, species: str):
        super().__init__(name, species)

    def carry_baby(self):
        return f"{self.name} the {self.species} is carrying its baby"

    def speak(self):
        return f"eeh eeh"
