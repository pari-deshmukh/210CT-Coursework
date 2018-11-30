"""
STUDENT NAME: PRANALI DESHMUKH
STUDENT ID: 8923910

COURSEWORK ASSIGNMENT 6:

Adapt the previous graph structure to support weighted connections and implement Dijkstra's algorithm. 

Please Note: I have used Python 2.7 for implementing the program.
"""


class Vertex(object):
    # Initialize the Vertex with the given value and no edges along with an infinite tentative weight and no previous vertex.
    def __init__(self, value):
        self.value = value
        # Initialize an edges dictionary where key: vertex, value: edge weight
        self.edges = {}
        self.tentativeWeight = float('inf')
        self.previousVertex = None


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

    def addEdge(self, v, w, weight):
        # If the edge between the two vertices v & w does not exist, then add it's weight, else print an error message.
        if w not in self.vertices.get(v).edges:
            self.vertices.get(v).edges[w] = weight
            self.vertices.get(w).edges[v] = weight
        else:
            print('Error: Edge %s-%s already exists' % (v, w))

    def dijkstra(self, source, destination):
        source = self.vertices[source]
        destination = self.vertices[destination]
        # Set the currently scanned node.
        CurrentVertex = source
        # Source has no distance from itself.
        source.tentativeWeight = 0
        visited = []
        while CurrentVertex != destination:
            # For all vertices, u, adjacent to the current vertex.
            for u in CurrentVertex.edges.keys():
                u = self.vertices[u]
                if CurrentVertex.tentativeWeight + u.edges[CurrentVertex.value] < u.tentativeWeight:
                    u.tentativeWeight = CurrentVertex.tentativeWeight + u.edges[CurrentVertex.value]
                    # Store the return path.
                    u.previousVertex = CurrentVertex

            visited.append(CurrentVertex)

            minimum = float('inf')

            for vertex in self.vertices.values():
                if vertex not in visited and vertex.tentativeWeight < minimum:
                    CurrentVertex = vertex
                    minimum = vertex.tentativeWeight

        return CurrentVertex.tentativeWeight


if __name__ == '__main__':

    # Generate graph
    g = Graph()

    # Add vertices to the graph.
    for vertex in map(chr,range(ord('A'),ord('H')+1)):
        g.addVertex(vertex)
    g.addVertex('S')

    # Add edges to the graph
    edges = [['A', 'S', 5],['S', 'G', 1],['S', 'C', 2],['G', 'F', 10],['G', 'H', 63],['H', 'E', 0],['A', 'B', 23],['C', 'F', 1],['C', 'E', 3],['C', 'D', 3]]
    for edge in edges:
        g.addEdge(edge[0], edge[1], edge[2])
    
    print('-------------------------------------------------------')
    print('WEIGHTED GRAPH:')
    print('-------------------------------------------------------')
    
    # Print the Graph's vertices.
    print('Vertices: ' + str(g.vertices.keys()))

    # Print all the edges for each vertex.
    print('\nEdges:')
    for vertex in map(chr,range(ord('A'),ord('H')+1)):
        print('\nEdges from vertex "' + vertex +'": ')
        for e in g.vertices.get(vertex).edges:
            print('[' + vertex + '-' + str(e) +'] -> ' + str(g.vertices.get(vertex).edges[e]))
    print('-------------------------------------------------------')
    print("Dijkstra's output: " + str(g.dijkstra('A', 'E')))
    print('-------------------------------------------------------')
