from typing import Generic, TypeVar
from .vertex import Vertex
from .edge import Edge

T = TypeVar('T')


class Graph(Generic[T]):
    def __init__(self) -> None:
        self.adj = {}

    def add_vertex(self, value: T) -> Vertex[T]:
        ...

    def add_edge(self, vertex1: Vertex, vertex2: Vertex, weight=None):
        ...

    def get_vertices(self) -> list[Vertex[T]]:
        ...

    def get_neighbors(self, vertex: Vertex[T]) -> list[Edge[T]]:
        ...

    def size(self) -> int:
        ...
