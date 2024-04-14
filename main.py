from networkx import Graph
from map import *
from SearchAlgorithms import *
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

mainGraph = Graph()

if __name__ == '__main__':
    config = read_map("map.txt")
    main_graph = init_graph(mainGraph, config)