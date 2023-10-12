from reptile import Reptile


class ReptileEnclosure:
    def __init__(self):
        self.reptiles = []

    def add_reptile(self, name, species):
        self.reptiles.append(Reptile(name, species))
