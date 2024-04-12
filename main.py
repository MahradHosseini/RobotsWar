from networkx import Graph
from map import *
from SearchAlgorithms import *
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

mainGraph = Graph()

if __name__ == '__main__':
    white_block_coords = read_map("map.txt")
    mainGraph = init_graph(mainGraph, white_block_coords)