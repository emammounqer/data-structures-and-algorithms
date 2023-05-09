from typing import Literal, Union
from stack_and_queue.queue import Queue
from stack_queue_animal_shelter.animal import Animal, Cat, Dog


class AnimalShelter:
    def __init__(self):
        self.cats = Queue[Cat]()
        self.dogs = Queue[Dog]()

    def enqueue(self, animal: Animal):
        if (isinstance(animal, Cat)):
            self.cats.enqueue(animal)
        if (isinstance(animal, Dog)):
            self.dogs.enqueue(animal)

    def dequeue(self, pref: Literal["cat", "dog"]):
        if (pref == "cat" and not self.cats.is_empty()):
            return self.cats.dequeue()
        if (pref == "dog" and not self.dogs.is_empty()):
            return self.dogs.dequeue()

        return None


shelter = AnimalShelter()

shelter.dequeue('cat')
