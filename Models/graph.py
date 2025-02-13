class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_graph(self, node, neighbor):
        if node not in self.graph:
            self.graph[node] = []
        self.graph[node].append(neighbor)