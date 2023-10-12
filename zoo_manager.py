from aviary import Aviary
from reptile_enclosure import ReptileEnclosure
from animal import Animal
from primate import Primate
from marsupial import Marsupial
from mammal import Mammal


class Zoo:
    def __init__(self):
        self.aviary = Aviary()
        self.reptile_enclosure = ReptileEnclosure()
        self.other_animals = []

    def add_animal(self, animal):
        name = input("Name: ")
        species = input("Species: ")
        if animal == "reptile":
            self.reptile_enclosure.add_reptile(name, species)
        elif animal == "bird":
            self.aviary.add_bird(name, species)
        elif animal == "primate":
            self.other_animals.append(Primate(name, species))
        elif animal == "marsupial":
            self.other_animals.append(Marsupial(name, species))
        elif animal == "mammal":
            self.other_animals.append(Mammal(name, species))
        else:
            self.other_animals.append(Animal(name, species))
