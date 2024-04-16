from itertools import combinations
from Map import *
from SearchAlgorithms import *
from Graphs import *

if __name__ == '__main__':
    config = read_map("map.txt")
    print(config)
    main_graph = init_main_graph(config)

    nodes = config['node_coordinates']
    shortest_path = []

    # Finding paths between each pair of nodes
    for (node1_id, node1_coord), (node2_id, node2_coord) in combinations(nodes.items(), 2):
        path = a_star_search(node1_coord, node2_coord, main_graph)
        if path:
            num_hops = len(path) - 1
            print(f"{node1_id} -> {node2_id}: Distance = {num_hops}, Path found: {path}")
            shortest_path.append((node1_id, node2_id, num_hops))
        else:
            print(f"{node1_id} -> {node2_id}: No path found")
            shortest_path.append((node1_id, node2_id, None))

    node_graph = init_node_graph(shortest_path)

    if 'A' not in nodes:
        raise ValueError("Node 'A' not found in the list of nodes.")

    initial_state = 'A'

    dfs_tour = depth_first_search(initial_state, node_graph)
    print("Tour sequence using Depth-First Search:")
    print(' -> '.join(dfs_tour))



