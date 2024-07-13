class Graph:
    def __init__(self, size, edges):
        self.adj_matrix = [[0] * size for _ in range(size)]
        self.size = size
        self.vertex_data = [''] * size
        self.minimal_spanning_tree = []
        
        for edge in edges:
            self.add_vertex_data(edge.start_node.id - 1, edge.start_node.id)
            self.add_vertex_data(edge.end_node.id - 1, edge.end_node.id)
            self.add_edge(edge.start_node.id - 1, edge.end_node.id - 1, edge.coust)

    def add_edge(self, u, v, weight):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = weight
            self.adj_matrix[v][u] = weight

    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data

    def prims_algorithm(self):
        in_mst = [False] * self.size
        key_values = [float('inf')] * self.size
        parents = [-1] * self.size

        key_values[0] = 0  # Starting vertex

        for _ in range(self.size):
            u = min((v for v in range(self.size) if not in_mst[v]), key=lambda v: key_values[v])
            in_mst[u] = True

            if parents[u] != -1:
                self.minimal_spanning_tree.append((self.vertex_data[parents[u]], self.vertex_data[u], self.adj_matrix[u][parents[u]]))
            for v in range(self.size):
                if 0 < self.adj_matrix[u][v] < key_values[v] and not in_mst[v]:
                    key_values[v] = self.adj_matrix[u][v]
                    parents[v] = u

    def run(self):
        self.prims_algorithm()
        return self.minimal_spanning_tree
