from ..graph import Graph, Vertex


def test_graph_depth_happy_path():
    graph = Graph[str]()
    a = graph.add_vertex('A')
    b = graph.add_vertex('B')
    c = graph.add_vertex('C')
    g = graph.add_vertex('G')
    d = graph.add_vertex('D')
    e = graph.add_vertex('E')
    h = graph.add_vertex('H')
    f = graph.add_vertex('F')

    graph.add_edge(a, b)
    graph.add_edge(a, d)
    graph.add_edge(b, c)
    graph.add_edge(b, d)
    graph.add_edge(c, g)
    graph.add_edge(d, e)
    graph.add_edge(d, h)
    graph.add_edge(d, f)
    graph.add_edge(h, f)

    actual = graph.graph_depth(a)
    expected = ['A', 'B', 'C', 'G', 'D', 'E', 'H', 'F']
    assert actual == expected


def test_graph_depth_one_node():
    graph = Graph[str]()
    a = graph.add_vertex('A')
    actual = graph.graph_depth(a)
    expected = ['A']
    assert actual == expected


def test_graph_depth_empty():
    graph = Graph[str]()
    actual = graph.graph_depth(None)
    expected = []
    assert actual == expected
