import matplotlib.pyplot as plt
import networkx as nx


# Takes the map config as input and converts the map into a graph
# Each node represents a white block
# Each edge represents an adjacency between the white blocks
def init_main_graph(config):
    graph = nx.Graph()
    for (x, y) in config['white_blocks']:
        node = (x, y)
        if node in config['node_coordinates'].items():
            graph.add_node(node)                            # add the node with Name= component
        else:
            graph.add_node(node)
        if (x, y + 1) in config['white_blocks']:            # we check its neighbours
            node1 = (x, y + 1)
            if node1 in config['node_coordinates']:
                graph.add_node(node1)                       # add the node with Name= component
            else:
                graph.add_edge(node, node1)
        if (x + 1, y) in config['white_blocks']:
            node1 = (x + 1, y)
            if node1 in config['node_coordinates']:
                graph.add_node(node1)                       # add the node with Name= component
            else:
                graph.add_edge(node, node1)

    nx.draw(graph, with_labels=True, node_color="red", node_size=750, font_color="white", font_size=10,
            font_family="Times New Roman", font_weight="bold", width=5, edge_color="black")
    plt.margins(0.1)
    plt.savefig('mainGraph.jpg')
    plt.show()
    return graph


def init_node_graph(shortest_path):
    node_graph = nx.Graph()

    for pair in shortest_path:
        node1, node2, distance = pair
        if distance is not None:
            node_graph.add_edge(node1, node2, weight=distance)
        else:
            node_graph.add_node(node1)
            node_graph.add_node(node2)

    if not nx.is_connected(node_graph):
        raise ValueError('The graph you have provided is not fully connected')

    pos = nx.spring_layout(node_graph)  # positions for all nodes

    # Nodes
    nx.draw_networkx_nodes(node_graph, pos, node_color='blue', node_size=1000)

    # Edges
    nx.draw_networkx_edges(node_graph, pos, width=1, edge_color='black')

    # Labels
    nx.draw_networkx_labels(node_graph, pos, font_size=10, font_color="white", font_family="Times New Roman",
                            font_weight="bold")

    # Edge weights
    edge_labels = nx.get_edge_attributes(node_graph, 'weight')
    nx.draw_networkx_edge_labels(node_graph, pos, edge_labels=edge_labels, font_size=15, font_color="red",
                                 font_weight="bold")

    plt.margins(0.2)
    plt.axis('off')
    plt.savefig('nodeGraph.jpg')
    plt.show()

    return node_graph
