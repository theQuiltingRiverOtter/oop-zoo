from mammal import Mammal


class Primate(Mammal):
    def __init__(self, name: str, species: str):
        super().__init__(name, species)

    def climb_trees(self):
        return f"{self.name} the {self.species} is climbing trees"

    def speak(self):
        return f"ooh ooh"


if __name__ == "__main__":
    bob = Primate("bob", "chimpazee")
    print(bob)
