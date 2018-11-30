"""
STUDENT NAME: PRANALI DESHMUKH
STUDENT ID: 8923910

COURSEWORK ASSIGNMENT 3:

Implement the structure for an unweighted, undirected graph G, where nodes consist of positive integers. Also, implement a function isPath(v, w), where v and w are vertices in the graph, to check if there is a path between the two nodes. The path found will be printed to a text file as a sequence of integer numbers (the node values).

Please Note: I have used Python 2.7 for implementing the program.
"""


class Vertex(object):
    # Initialize the Vertex with the given value and no edges.
    def __init__(self, value):
        self.value = value
        self.edges = []


class Graph(object):
    # Initialize the Graph Object with no vertices.
    def __init__(self):
        self.vertices = {}

    def addVertex(self, value):
        # If the vertex is not in the graph, add it, else print an error message.
        if value not in self.vertices:
            self.vertices[value] = Vertex(value)
        else:
            print('Error: Vertex %s already exists' % value)

    def addEdge(self, v, w):
        # If the edge between the two vertices v & w does not exist, then add it, else print an error message.
        if w not in self.vertices.get(v).edges:
            self.vertices.get(v).edges.append(w)
            self.vertices.get(w).edges.append(v)
        else:
            print('Error: Edge %s-%s already exists' % (v, w))

    def isPath(self, v, w):
        # Perform a modified Depth-First-Search, that checks whether the two nodes v & w are connected.
        stack = []
        visited = []
        Found = False
        stack.append(v)
        while len(stack) > 0:
            u = stack.pop()
            # If the target vertex w is found then mark it as visited and set Found to true.
            if u == w:
                visited.append(u)
                Found = True
                break

            if u not in visited:
                # If the current vertex hasn't been visited yet, then mark it as visited.
                visited.append(u)
                # Check if the current vertex is a dead end, i.e. if there is only one edge connected to the current vertex, then remove it from the path.
                if len(self.vertices.get(u).edges) == 1:
                    visited.pop()
                # Add all edges of the current vertex to the stack.
                for e in self.vertices.get(u).edges:
                    stack.append(e)

        # Save the result to a file.
        output_file = open('path.txt', 'w')
        if Found:
            output_file.write(str('Path found from node ' + str(v) + ' to node ' + str(w) + ' is: ' + str(visited) + '.'))
        else:
            output_file.write(str('Path between nodes ' + str(v) + ' and ' + str(w) + ' not found!'))
        output_file.close()
        return Found


if __name__ == '__main__':

    # Generate graph
    g = Graph()

    # Add nine vertices to the graph.
    for vertex in range(1,10):
        g.addVertex(vertex)

    # Add edges to the graph
    edges = [[1, 9],[9, 7],[9, 3],[7, 6],[7, 8],[8, 5],[1, 2],[3, 6],[3, 5],[3, 4]]
    for edge in edges:
        g.addEdge(edge[0], edge[1])
    
    print('-----------------------------------------------')
    print('UNWEIGHTED, UNDIRECTED GRAPH:')
    print('-----------------------------------------------')
    
    # Print the Graph's vertices.
    print('Vertices: ' + str(g.vertices.keys()))

    # Print all the edges for each vertex.
    print('\nEdges:')
    for vertex in range(1,10):
        print('\nEdges from vertex "' + str(vertex) +'": ')
        for e in g.vertices.get(vertex).edges:
            print('[' + str(vertex) + '-' + str(e) +']')
    print('-----------------------------------------------')
    print('isPath(1, 5): ' + str(g.isPath(1, 5)))
    print('-----------------------------------------------')
