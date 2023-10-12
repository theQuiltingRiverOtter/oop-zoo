from bird import Bird


class Aviary:
    def __init__(self):
        self.birds = []

    def add_bird(self, name, species):
        self.birds.append(Bird(name, species))
