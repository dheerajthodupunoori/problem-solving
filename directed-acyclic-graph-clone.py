#directed graph

from collections import deque

class GraphNode:

    def __init__(self,value):

        self.val = value
        self.adjacent = []

class GraphOperations:

    def __init__(self):
        print("Graph operations classe is initialized")
        self.graph = set()

    def addEdge(self,source,destination):

        # print("Adding edge from {source} to {destination}".format(source=source.val,destination=destination.val))

        if source not in self.graph:

            self.graph.add(source)
        
        source.adjacent.append(destination)

        # print("Edge added from {source} to {destination}".format(source=source.val,destination=destination.val))

    def printGraph(self,graph):

        for node in graph:

            print("Parent - {value} and {object}".format(value=node.val,object=node))

            for adjacent in node.adjacent:

                print("       ------>{value} and {object}".format(value=adjacent.val,object=adjacent))


    def cloneDAG(self,source,visited):

        queue = deque()
        queue.append(source)

        clone = GraphNode(source.val)

        visited[source] = clone

        while len(queue) > 0:

            popped = queue.popleft()

            root = visited[popped]

            for adjacent in popped.adjacent:

                adjacent_clone = None

                if adjacent not in visited:

                    adjacent_clone = GraphNode(adjacent.val)
                    visited[adjacent] = adjacent_clone

                else:
                    adjacent_clone = visited[adjacent]
                
                queue.append(adjacent)
                root.adjacent.append(adjacent_clone)


if __name__=="__main__":
    # print("Directed Acyclic Graph Cloning.")

    graph = GraphOperations()

    one = GraphNode(1)
    two = GraphNode(2)
    three = GraphNode(3)
    four = GraphNode(4)

    nodes = [one,two,three,four]

    graph.addEdge(one,two)
    graph.addEdge(three,two)

    print("Graph before cloning")

    graph.printGraph(nodes)

    visited = dict()

    for node in nodes:

        if node not in visited:

            graph.cloneDAG(node,visited)

    print("*************************************")
    print("Graph after cloning")

    print(len(visited.values()))
    cloned_graph =visited.values()
    graph.printGraph(cloned_graph)

    