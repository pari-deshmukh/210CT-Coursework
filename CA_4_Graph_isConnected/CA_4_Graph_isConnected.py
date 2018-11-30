"""
STUDENT NAME: PRANALI DESHMUKH
STUDENT ID: 8923910

COURSEWORK ASSIGNMENT 4:

Using the graph structure previously implemented, implement a function isConnected(G) to check whether or not the graph is strongly connected. The output should be simply 'yes'
or 'no'.

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

    def checkPath(self, v, w):
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
        return Found

    def isConnected(self):
        # Check if the graph is strongly connected, by running the isPath function between all it's nodes.
        Connected = True
        for v in self.vertices:
            for w in self.vertices:
                if v != w:
                    # Change the result to "False" if one instance of isPath returns "False". 
                    Connected *= self.checkPath(v, w)
        if Connected:
            return 'Yes'
        else:
            return 'No'


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
    
    print('-------------------------------------')
    print('UNWEIGHTED, UNDIRECTED GRAPH:')
    print('-------------------------------------')
    
    # Print the Graph's vertices.
    print('Vertices: ' + str(g.vertices.keys()))

    # Print all the edges for each vertex.
    print('\nEdges:')
    for vertex in range(1,10):
        print('\nEdges from vertex "' + str(vertex) +'": ')
        for e in g.vertices.get(vertex).edges:
            print('[' + str(vertex) + '-' + str(e) +']')
    print('-------------------------------------')
    print('isConnected: ' + g.isConnected())
    print('-------------------------------------')
