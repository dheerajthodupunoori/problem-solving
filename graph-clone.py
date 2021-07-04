#for undirected graph

from collections import deque

class GraphNode:

    def __init__(self,value):

        self.val = value
        self.adjacent = []

class Graph:

    def __init__(self,source):
        self.source = source
        self.visited = dict()

    def doBfs(self,source,visited,answer):

        queue = deque()
        queue.append(source)
        answer.append(source.val)

        visited.add(source)

        print("Graph Node - ",source.val,source)

        while len(queue)>0:

            popped = queue.popleft()

            for adjacent in popped.adjacent:
                
                if adjacent not in visited:

                    queue.append(adjacent)
                    answer.append(adjacent.val)
                    visited.add(adjacent)
                    print("Graph Node - ",adjacent.val,adjacent)

        return answer


    def cloneGraph(self):

        if self.source is None:
            return

        queue = deque()
        queue.append(self.source)
        newSource = GraphNode(self.source.val)

        self.visited[self.source] = newSource

        while len(queue)>0:

            popped = queue.popleft()
            clonedNode = self.visited[popped]

            for adjacent in popped.adjacent:
                if adjacent not in self.visited:
                    clonedAdjacent = GraphNode(adjacent.val)
                    self.visited[adjacent] = clonedAdjacent
                    queue.append(adjacent)
                    clonedNode.adjacent.append(clonedAdjacent)

        return self.visited[self.source]

    def addEdge(self,source,destination):

        if source not in self.graph:
            self.graph[source] = []
            self.graph[source].append(destination)
        else:
            self.graph[source].append(destination)
        print("Added edge from {source} to {destination}".format(source=source,destination=destination))

if __name__=="__main__":

    one = GraphNode(1)
    two = GraphNode(2)
    three = GraphNode(3)
    four = GraphNode(4)

    total_nodes = [one,two,three,four]

    one_adjacent = [two,four]
    one.adjacent = one_adjacent

    two_adjacent = [one,three]
    two.adjacent = two_adjacent

    three_adjacent = [two,four]
    three.adjacent = three_adjacent

    four_adjacent = [three,one]
    four.adjacent = four_adjacent

    graph = Graph(one)
    newSource = graph.cloneGraph()

    sourceGraphVisited = set()
    answer = []

    for node in total_nodes:

        if node not in sourceGraphVisited:

            graph.doBfs(node,sourceGraphVisited,answer)

    print("Before cloning the graph - " , answer)

    answer = []
    clonedGraphVisited = set()

    for node in graph.visited.values():

        if node not in clonedGraphVisited:

            graph.doBfs(node,clonedGraphVisited,answer)

    print("After cloning the graph - ", answer)

   
    print(len(graph.visited))