from typing import Literal
from stack_queue_animal_shelter.animal import Animal


class AnimalShelter:
    def __init__(self):
        self.animals: list[Animal] = []

    def enqueue(self, animal: Animal):
        self.animals.append(animal)

    def dequeue(self, pref: Literal["cat", "dog"]):
        if (pref == "cat"):
            return self.get_first_of_species("cat")
        if (pref == "dog"):
            return self.get_first_of_species("dog")

        return None

    def get_first_of_species(self, species: Literal["cat", "dog"]):
        for i, animal in enumerate(self.animals):
            if animal.species == species:
                return self.animals.pop(i)

        return None


shelter = AnimalShelter()

shelter.dequeue('cat')
