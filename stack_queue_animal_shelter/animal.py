class Animal:
    def __init__(self, species, name) -> None:
        self.species = species
        self.name = name


class Dog(Animal):
    def __init__(self, name):
        super().__init__("dog", name)


class Cat(Animal):
    def __init__(self, name):
        super().__init__("cat", name)
