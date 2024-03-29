from typing import Generic, TypeVar, Optional
from stack_and_queue.queue import Queue
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

    def breadth_first(self, vertex: Optional[Vertex[T]]) -> list[Vertex[T]]:
        """Returns a list of all the vertices in the graph in breadth first order"""
        if vertex is None:
            return []

        traverse_list = []
        queue = Queue[Vertex]()
        queue.enqueue(vertex)
        visited_vertex = set([vertex])

        while not queue.is_empty():
            curr = queue.dequeue()
            traverse_list.append(curr)

            neighbors = self._adjacency_list[curr]

            for neighbor in neighbors:
                if neighbor.vertex not in visited_vertex:
                    queue.enqueue(neighbor.vertex)
                    visited_vertex.add(neighbor.vertex)

        return traverse_list

    def get_vertex(self, value: T) -> Optional[Vertex[T]]:
        for vertex in self._adjacency_list.keys():
            if vertex.value == value:
                return vertex

    def graph_depth(self, root: Optional[Vertex[T]]):
        '''Returns a list of all the vertices in the graph in depth first order'''
        if root is None:
            return []
        visited = set([root])
        traversed = [root.value]

        def rec(node: Vertex[T]):
            neighbors = self.get_neighbors(node)
            for edge in neighbors:
                if not edge.vertex in visited:
                    traversed.append(edge.vertex.value)
                    visited.add(edge.vertex)
                    rec(edge.vertex)
        rec(root)
        return traversed

    def __str__(self):
        output = '\n'
        for vertex in self._adjacency_list.keys():
            output += f'{vertex} -> '
            for edge in self._adjacency_list[vertex]:
                output += f'{edge.vertex} -----> '
            output += 'None \n'
        return output
