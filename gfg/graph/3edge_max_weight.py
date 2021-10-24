class Graph:

    def __init__(self, vertices):
        self.v = vertices
        self.graph = {}
        for i in range(1, self.v+1):
            self.graph.setdefault(i, [])
        self.maximum_weight = 0
        self.visited = set()
        self.visited_edges = set()

    def add_edge(self, edge):
        # self.graph.setdefault(edge[0], [])
        self.graph[edge[0]].append([edge[1], edge[2]])

    def find_3edge_max_weight(self):
        print(self.graph)
        for node in range(1, self.v+1):
            if node not in self.visited:
                self.visited_edges = set()
                path = []
                self.dfs(path, node)

        print("Maximum 3-edge weight - ", self.maximum_weight)

    def dfs(self, path, node):
        print(self.maximum_weight, path, node)

        if len(path) >= 3:
            self.maximum_weight = max(self.maximum_weight, sum([p[2] for p in path[-3:]]))

        # if node not in self.graph:
        #     return

        self.visited.add(node)

        for adjacent in self.graph[node]:
            if (adjacent[0], adjacent[1]) not in self.visited_edges:
                self.visited_edges.add((adjacent[0], adjacent[1]))
                path.append([node, adjacent[0], adjacent[1]])
                self.dfs(path, adjacent[0])
                path.pop()


graph = Graph(8)
graph.add_edge([1, 2, 3])
graph.add_edge([2, 3, 5])
graph.add_edge([3, 4, 7])
graph.add_edge([5, 6, 2])
graph.add_edge([6, 7, 4])
graph.add_edge([7, 8, 11])
graph.find_3edge_max_weight()



graph = Graph(4)
graph.add_edge([1, 2, 1])
graph.add_edge([2, 3, 1])
graph.add_edge([3, 4, 1])
graph.add_edge([4, 1, 1])
graph.add_edge([1, 3, 10])
# graph.add_edge([7, 8, 11])
graph.find_3edge_max_weight()


graph = Graph(5)
graph.add_edge([1, 2, 5])
graph.add_edge([3, 4, 5])
graph.add_edge([4, 5, 5])
# graph.add_edge([4, 1, 1])
# graph.add_edge([1, 3, 10])
# graph.add_edge([7, 8, 11])
graph.find_3edge_max_weight()
