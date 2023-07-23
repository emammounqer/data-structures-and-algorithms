from pytest import fixture
from ..graph import Graph
from ..graph_business_trip import graph_business_trip


@fixture()
def graph():
    # pandora ---150--- arendelle
    #       \82        99/        \42
    #         Metroville ---105-- Monstroplolis
    #        /37        \26         /73
    #   Narnia  --250---  Naboo

    graph = Graph[str]()
    pandora = graph.add_vertex('Pandora')
    arendelle = graph.add_vertex('Arendelle')
    metroville = graph.add_vertex('Metroville')
    monstroplolis = graph.add_vertex('Monstroplolis')
    narnia = graph.add_vertex('Narnia')
    naboo = graph.add_vertex('Naboo')

    graph.add_edge(pandora, arendelle, 150)
    graph.add_edge(pandora, metroville, 82)
    graph.add_edge(arendelle, metroville, 99)
    graph.add_edge(arendelle, monstroplolis, 42)
    graph.add_edge(metroville, narnia, 37)
    graph.add_edge(metroville, naboo, 26)
    graph.add_edge(metroville, monstroplolis, 105)
    graph.add_edge(monstroplolis, naboo, 73)
    graph.add_edge(narnia, naboo, 250)

    return graph


def test_graph_business_trip_empty(graph: Graph[str]):
    actual = graph_business_trip(graph, [])
    expected = 0
    assert actual == expected


def test_graph_business_trip_one_city(graph: Graph[str]):
    actual = graph_business_trip(graph, ['Pandora'])
    expected = 0
    assert actual == expected


def test_graph_business_trip_two_cities(graph: Graph[str]):
    actual = graph_business_trip(graph, ['Pandora', 'Arendelle'])
    expected = 150
    assert actual == expected


def test_graph_business_trip(graph: Graph[str]):

    actual = graph_business_trip(
        graph, ['Pandora', 'Arendelle', 'Monstroplolis'])
    expected = 192
    assert actual == expected


def test_graph_business_trip_not_connected(graph: Graph[str]):

    actual = graph_business_trip(
        graph, ['Pandora', 'Arendelle', 'Naboo'])
    expected = None
    assert actual == expected
