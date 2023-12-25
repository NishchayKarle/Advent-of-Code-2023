import networkx as nx

def parse_input(data):
    graph = nx.Graph()
    
    for line in data:
        l, r = line.split(":")
        for node in r.strip().split():
            graph.add_edge(l, node)
            graph.add_edge(node, l)
    
    return graph

def part1(graph: nx.Graph):
    min_edge_cut = nx.minimum_edge_cut(graph)
    graph.remove_edges_from(min_edge_cut)
    l, r = nx.connected_components(graph)

    return len(l) * len(r)

def part2(data):
    pass

if __name__ == "__main__":
    with open("sample.txt", "r") as f:
        sample_data = parse_input(f.read().splitlines())

    with open("input.txt", "r") as f:
        data = parse_input(f.read().splitlines())

    print(part1(sample_data))
    print(part1(data))

    # print(part2(sample_data))
    # print(part2(data))