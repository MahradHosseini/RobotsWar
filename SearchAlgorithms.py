import matplotlib.pyplot as plt
import networkx as nx
import numpy as np


def init_graph(graph, white_block_coords):
    for (x, y) in white_block_coords:
        node = (x, y)
        graph.add_node(node)
        if (x, y+1) in white_block_coords:
            node1 = (x, y+1)
            graph.add_edge(node, node1)
        if (x+1, y) in white_block_coords:
            node1 = (x+1, y)
            graph.add_edge(node, node1)

    nx.draw(graph, with_labels=True, node_color="red", node_size=2000, font_color="white", font_size=20,
            font_family="Times New Roman", font_weight="bold", width=5, edge_color="black")
    plt.margins(0.2)
    plt.show()
