from networkx import Graph
from map import *
from SearchAlgorithms import *

mainGraph = Graph()

if __name__ == '__main__':
    config = read_map("map.txt")
    main_graph = init_graph(mainGraph, config)
    print(a_star_search("D", "A", main_graph))
