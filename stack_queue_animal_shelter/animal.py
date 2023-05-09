from typing import Literal


class Animal:
    def __init__(self, species: Literal["cat", "dog"], name: str) -> None:
        self.species: Literal["cat", "dog"] = species
        self.name = name
