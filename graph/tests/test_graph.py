from ..graph import Graph, Vertex


def test_graph_add_node():
    graph = Graph[str]()
    vertex = graph.add_vertex('test 1')

    assert vertex in graph._adjacency_list
    assert graph._adjacency_list[vertex] == []


def test_graph_add_node_return_value():
    graph = Graph[str]()
    vertex = graph.add_vertex('test 1')
    assert isinstance(vertex, Vertex)
    assert vertex.value == 'test 1'


def test_graph_add_multiple_nodes():
    graph = Graph[str]()
    vertex1 = graph.add_vertex('test 1')
    vertex2 = graph.add_vertex('test 2')

    assert vertex1 in graph._adjacency_list
    assert graph._adjacency_list[vertex1] == []

    assert vertex2 in graph._adjacency_list
    assert graph._adjacency_list[vertex2] == []


def test_graph_add_edge():
    graph = Graph[str]()
    vertex1 = graph.add_vertex('test 1')
    vertex2 = graph.add_vertex('test 2')

    graph.add_edge(vertex1, vertex2)

    assert vertex2 == graph._adjacency_list[vertex1][0].vertex
    assert vertex1 == graph._adjacency_list[vertex2][0].vertex


def test_graph_add_edge_with_weight():
    graph = Graph[str]()
    vertex1 = graph.add_vertex('test 1')
    vertex2 = graph.add_vertex('test 2')

    graph.add_edge(vertex1, vertex2, 10)

    assert graph._adjacency_list[vertex1][0].weight == 10
    assert graph._adjacency_list[vertex2][0].weight == 10


def test_graph_get_vertices():
    graph = Graph[str]()
    vertex1 = graph.add_vertex('test 1')
    vertex2 = graph.add_vertex('test 2')

    vertices = graph.get_vertices()

    assert vertex1 in vertices
    assert vertex2 in vertices


def test_graph_get_neighbors():
    graph = Graph[str]()
    vertex1 = graph.add_vertex('test 1')
    vertex2 = graph.add_vertex('test 2')

    graph.add_edge(vertex1, vertex2)

    neighbors = graph.get_neighbors(vertex1)

    assert neighbors[0].vertex == vertex2
    assert neighbors[0].weight == None

    neighbors = graph.get_neighbors(vertex2)

    assert neighbors[0].vertex == vertex1
    assert neighbors[0].weight == None


def test_graph_size():
    graph = Graph[str]()
    vertex1 = graph.add_vertex('test 1')
    vertex2 = graph.add_vertex('test 2')
    graph.add_edge(vertex1, vertex2)

    assert graph.size() == 2
