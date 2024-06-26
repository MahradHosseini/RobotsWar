from collections import deque
from queue import PriorityQueue
import networkx as nx

"""
Implementation of the A* Search Algorithm
Takes a starting state, a goal state, and a graph
Returns the path with minimum distance, or None if no path exists
"""


def a_star_search(initial_state, goal_state, graph):
    queue = PriorityQueue()  # define a queue
    queue.put((0, [initial_state]))  # we put initial state with 0 f in the queue
    while queue.qsize() != 0:  # while not empty
        path = queue.get()[1]  # getting 2nd element
        current_state = path[-1]  # current_state is lastly added element
        if current_state == goal_state:  # if it is goal_state
            return path  # return path if found

            # extending path every possible way
        for next_state in successors(current_state, graph):  # while every successor
            if next_state not in path:  # if the successor paths are not in path
                new_path = list(path)  # create a list for a new path
                new_path.append(next_state)  # append the state to our new path
                g = len(new_path) - 1  # Real cost of the path until now
                h = manhattan_distance(next_state, goal_state)  # Estimate of the remaining distance
                f = g + h  # heuristics + g
                queue.put((f, new_path))  # new path to the queue

    return None  # return failure


"""
Implementation of the Depth First Search Algorithm
Takes a starting state and a graph
Returns the first path found or None if no path exists
"""


def depth_first_search(initial_state, graph):
    # Using stack
    stack = deque([[initial_state]])

    while stack:
        # Poping from Stack
        path = stack.pop()
        current_node = path[-1]

        if len(path) > 1 and current_node == initial_state and len(set(path)) == len(graph.nodes()):
            return path

        # Creating a list of neighbor nodes
        neighbors = list(nx.neighbors(graph, current_node))

        for neighbor in neighbors:
            # If there is an unvisited node, or
            # If returns back to initial point and all the nodes are visited
            if neighbor not in path or (neighbor == initial_state and len(set(path)) == len(graph.nodes())):
                new_path = list(path) + [neighbor]
                stack.append(new_path)

    return None


"""
Implementation of the Uniform-Cost Search Algorithm
Takes a starting state and a graph
Returns the best path found with minimum cost or None if no path exists
"""


def uniform_cost_search(initial_state, graph):
    # Using Priority Queue with Cost as the evaluating value
    queue = PriorityQueue()
    queue.put((0, [initial_state]))

    while not queue.empty():
        # Pop from the Queue
        cost, path = queue.get()
        terminal_node = path[-1]
        # If goal state is found, return
        if is_goal_state(graph, path):
            return path, cost

        for neighbor in graph.neighbors(terminal_node):
            # If there is an unvisited node, or
            # If returns back to initial point and all the nodes are visited
            if neighbor not in path or (neighbor == initial_state and len(set(path)) == len(graph.nodes())):
                new_cost = cost + graph[terminal_node][neighbor]['weight']
                new_path = path + [neighbor]
                queue.put((new_cost, new_path))
    return None, None


"""
Checks if a state is a valid goal state for UCS
Takes the graph and the current found path
Returns true if the state is a valid goal state, false otherwise
"""


def is_goal_state(graph, tour):
    # If the nodes in path are equal to all nodes of the graph, and
    # If first and last nodes are the same (initial_node)
    return set(tour) == set(graph.nodes()) and tour[0] == tour[-1]


"""
Creates a list of node's successors
"""


def successors(state, graph):
    x, y = state
    successor = []
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # covering every direction
    for xx, yy in directions:  # going over directions
        if (x + xx, y + yy) in graph:  # checks if the new coordinate is white
            successor.append((x + xx, y + yy))  # append the successor

    return successor


"""
Finds manhattan distance between two points (x1,y1) and (x2,y2)
"""


def manhattan_distance(node1, node2):
    # |
    # |
    # |________   this is how it works
    return abs(node1[0] - node2[0]) + abs(node1[1] - node2[1])
    # x coordinate - x coordinate + y coordinate - y coordinate
