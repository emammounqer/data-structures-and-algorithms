from typing import Optional, TypeVar, Generic
from .vertex import Vertex


T = TypeVar('T')


class Edge(Generic[T]):
    def __init__(self, vertex: Vertex[T], weight: Optional[int] = None) -> None:
        self.vertex = vertex
        self.weight = weight
