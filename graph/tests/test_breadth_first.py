from ..graph import Graph


def test_breadth_first():
    # pandora -------- arendelle
    #                  /        \
    #         Metroville -------- Monstroplolis
    #         /        \         /
    #   Narnia  --------  Naboo
    # adjacency list:
    # {
    #   pandora: [arendelle],
    #   arendelle: [pandora, metroville, monstroplolis],
    #   metroville: [arendelle, narnia, naboo, monstroplolis],
    #   monstroplolis: [arendelle, metroville, naboo],
    #   narnia: [metroville, naboo],
    #   naboo: [metroville, monstroplolis, narnia]
    # }
    
    g = Graph()
    pandora = g.add_vertex('Pandora')
    arendelle = g.add_vertex('Arendelle')
    metroville = g.add_vertex('Metroville')
    monstroplolis = g.add_vertex('Monstroplolis')
    narnia = g.add_vertex('Narnia')
    naboo = g.add_vertex('Naboo')

    g.add_edge(pandora, arendelle)
    g.add_edge(arendelle, metroville)
    g.add_edge(arendelle, monstroplolis)
    g.add_edge(metroville, narnia)
    g.add_edge(metroville, naboo)
    g.add_edge(metroville, monstroplolis)
    g.add_edge(monstroplolis, naboo)
    g.add_edge(narnia, naboo)

    actual = g.breadth_first(pandora)
    expected = [pandora, arendelle, metroville,
                monstroplolis, narnia, naboo]
    assert actual == expected


def test_breadth_first_empty():
    g = Graph()
    actual = g.breadth_first(None)
    expected = []
    assert actual == expected
