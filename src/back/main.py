from queue import Queue
from copy import deepcopy
from src.front.node import Node
from src.front.edge import Edge

class Graph:

    def __init__(self, nodes: list, edges: list):
        self.nodes = nodes
        self.edges = edges
        self.adj = {}

    def show(self):
        print("Nodes:")
        for node in self.nodes:
            print(node.id, node.pos)
        print("Edges:")
        for edge in self.edges:
            print(edge.start, edge.end, edge.coust)
        # for node in nodes:
        #     self.adj[node.id] = []
        # for edge in edges:
        #     self.adj[edge[0]].append(edge[1])