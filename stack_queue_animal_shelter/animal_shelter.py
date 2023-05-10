from typing import Literal, Union
from stack_queue_animal_shelter.animal import Animal


class AnimalShelter:
    """ A shelter that holds dogs and cats, and returns the first animal that matches the preference"""

    def __init__(self):
        self.animals: list[Animal] = []

    def enqueue(self, animal: Animal):
        """Add an animal to the shelter"""
        self.animals.append(animal)

    def dequeue(self, pref: Union[Literal["cat", "dog"], None] = None):
        """Remove the first animal from the shelter that matches the preference, or the first animal if no preference is given"""
        if pref is None and len(self.animals) > 0:
            return self.animals.pop(0)

        for i, animal in enumerate(self.animals):
            if animal.species == pref:
                return self.animals.pop(i)

        return None
