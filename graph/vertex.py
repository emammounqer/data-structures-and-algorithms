from typing import Generic, TypeVar

T = TypeVar('T')


class Vertex(Generic[T]):
    def __init__(self, value: T) -> None:
        self.value = value

    def __str__(self) -> str:
        return str(self.value)
    
    def __repr__(self) -> str:
        return str(self.value)
