from animal import Animal


class Bird(Animal):
    def __init__(self, name: str, species: str, wingspan: float):
        super().__init__(name, species)
        self.wingspan = wingspan

    def speak(self):
        print("tweet tweet")
