from graph.graph import Graph


def graph_business_trip(graph: Graph[str], cities: list[str]):
    cost = 0
    for i in range(len(cities) - 1):
        curr_vertex = graph.get_vertex(cities[i])
        dist_vertex = graph.get_vertex(cities[i+1])
        if not curr_vertex or not dist_vertex:
            return None

        trip_cost = get_weight(graph, curr_vertex, dist_vertex)
        if trip_cost is None:
            return None
        cost += trip_cost

    return cost


def get_weight(graph: Graph[str], curr_vertex, dist_vertex):
    neighbors = graph.get_neighbors(curr_vertex)

    for neighbor in neighbors:
        if neighbor.vertex == dist_vertex:
            return neighbor.weight
