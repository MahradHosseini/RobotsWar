import math
from collections import deque
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from queue import PriorityQueue, Queue


def manhattan_distance(node1, node2):
    return abs(node1[0] - node2[0]) + abs(node1[1] - node2[1])


def init_graph(graph, config):
    for (x, y) in white_block_coords:
        node = (x, y)
        if node in named_nodes:
            graph.add_node(node, Name=named_nodes(node).Name)
        else:
            graph.add_node(node)
        if (x, y + 1) in white_block_coords:
            node1 = (x, y + 1)
            if node1 in named_nodes:
                graph.add_node(node, node1, Name=named_nodes(node1).Name)
            else:
                graph.add_edge(node, node1)
        if (x + 1, y) in white_block_coords:
            node1 = (x + 1, y)
            if node1 in named_nodes:
                graph.add_node(node, node1, Name=named_nodes(node1).Name)
            else:
                graph.add_edge(node, node1)

    nx.draw(graph, with_labels=True, node_color="red", node_size=1000, font_color="white", font_size=10,
            font_family="Times New Roman", font_weight="bold", width=5, edge_color="black")
    plt.margins(0.2)
    plt.show()
    return graph


def a_star_search(initial_state, goal_state, graph):
    queue = PriorityQueue()                 # define a queue
    queue.put((0, [initial_state]))         # we put initial state with 0 f in the queue
    while not queue.empty:                  # while
        path = queue.get()[1]               # getting 2nd element
        current_state = path[-1]            # current_state is lastly added element
        if current_state == goal_state:     # if it is goal_state
            return path                     # return path if found

            # extending path every possible way
        for next_state in successors(current_state, graph):  # while every successor
            if next_state not in path:                          # if the successor paths are not in path
                new_path = list(path)                           # create a list for a new path
                new_path.append(next_state)                     # append the state to our new path
                g = len(new_path) - 1                           # Real cost of the path until now
                h = manhattan_distance(next_state, goal_state)  # Estimate of the remaining distance
                f = g + h                                       # heuristics + g
                queue.put((f, new_path))                        # new path to the queue

    return None                                                 # return failure


def successors(state, graph):
    x, y = state.x, state.y
    successor = []
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]             # covering every direction
    for xx, yy in directions:                                   # going over directions
        if (x + xx, y + yy) in graph:                           # checks if the new coordinate is white
            successor.append((x + xx, y + yy))                  # append the successor

    return successor
