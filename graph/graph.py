from typing import Generic, TypeVar, Optional
from .vertex import Vertex
from .edge import Edge

T = TypeVar('T')


class Graph(Generic[T]):
    def __init__(self) -> None:
        self._adjacency_list: dict[Vertex[T], list[Edge[T]]] = {}

    def add_vertex(self, value: T) -> Vertex[T]:
        """Adds a vertex to the graph"""
        vertex = Vertex(value)
        self._adjacency_list[vertex] = []
        return vertex

    def add_edge(self, vertex1: Vertex, vertex2: Vertex, weight: Optional[int] = None):
        """Adds an edge between two vertices in the graph"""
        if vertex1 not in self._adjacency_list:
            raise KeyError('vertex1 not in graph')
        if vertex2 not in self._adjacency_list:
            raise KeyError('vertex2 not in graph')

        edge1 = Edge(vertex2, weight)
        self._adjacency_list[vertex1].append(edge1)

        edge2 = Edge(vertex1, weight)
        self._adjacency_list[vertex2].append(edge2)

    def get_vertices(self) -> list[Vertex[T]]:
        """Returns a list of all the vertices in the graph"""
        return list(self._adjacency_list.keys())

    def get_neighbors(self, vertex: Vertex[T]) -> list[Edge[T]]:
        """Returns a list of all the edges connected to the given vertex"""
        if vertex not in self._adjacency_list:
            raise KeyError('vertex not in graph')

        return self._adjacency_list[vertex]

    def size(self) -> int:
        """Returns the number of vertices in the graph"""
        return len(self._adjacency_list)

    def __str__(self):
        output = '\n'
        for vertex in self._adjacency_list.keys():
            output += f'{vertex} -> '
            for edge in self._adjacency_list[vertex]:
                output += f'{edge.vertex} -----> '
            output += 'None \n'
        return output
