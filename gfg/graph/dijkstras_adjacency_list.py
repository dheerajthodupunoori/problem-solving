import heapq
import sys


class Graph:

    def __init__(self, vertices):
        self.graph = {}
        self.v = vertices
        self.distance = [sys.maxsize] * self.v
        self.visited = [False] * self.v

    def addEdge(self, edge):
        self.graph.setdefault(edge[0], [])
        self.graph.setdefault(edge[1], [])

        self.graph[edge[0]].append([edge[1], edge[2]])
        self.graph[edge[1]].append([edge[0], edge[2]])

        # print("Added edge from {v1} to {v2} with weight {weight}".format(v1=edge[0], v2=edge[1], weight=edge[2]))
        # print("Added edge from {v1} to {v2} with weight {weight}".format(v1=edge[1], v2=edge[2], weight=edge[2]))

    def get_min(self):

        min_index = 0
        minimum = sys.maxsize

        for vertex in range(self.v):
            if not self.visited[vertex] and self.distance[vertex] < minimum:
                minimum = self.distance[vertex]
                min_index = vertex

        return min_index

    def dijkstras(self, source):
        self.distance[source] = 0
        for _ in range(self.v):
            next_vertex = self.get_min()
            print("Next choosen vertex - ", next_vertex)
            self.visited[next_vertex] = True
            if next_vertex in self.graph:
                for adjacent in self.graph[next_vertex]:
                    print(adjacent)
                    if self.distance[adjacent[0]] > self.distance[next_vertex] + adjacent[1]:
                        self.distance[adjacent[0]] = self.distance[next_vertex] + adjacent[1]

        print(self.distance)


graph = Graph(9)
graph.addEdge([0, 1, 4])
graph.addEdge([0, 7, 8])
graph.addEdge([1, 2, 8])
graph.addEdge([1, 7, 11])
graph.addEdge([2, 3, 7])
graph.addEdge([2, 8, 2])
graph.addEdge([2, 5, 4])
graph.addEdge([3, 4, 9])
graph.addEdge([3, 5, 14])
graph.addEdge([4, 5, 10])
graph.addEdge([5, 6, 2])
graph.addEdge([6, 7, 1])
graph.addEdge([6, 8, 6])
graph.addEdge([7, 8, 7])
print(graph.graph)
graph.dijkstras(0)
