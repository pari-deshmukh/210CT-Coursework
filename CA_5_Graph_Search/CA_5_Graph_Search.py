"""
STUDENT NAME: PRANALI DESHMUKH
STUDENT ID: 8923910

COURSEWORK ASSIGNMENTS 5:

Implement BFS and DFS traversals for the above graph structure. Save the nodes traversed in sequence to a text file.

Please Note: I have used Python 2.7 for implementing the program.
"""


from collections import deque

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

    def bfs(self, v):
        # Perform a Breadth-First-Search, that traverses the graph from the vertex v.
        queue = deque()
        visited = []
        queue.append(v)
        while len(queue) > 0:
            u = queue.popleft()
            if u not in visited:
                # If the current vertex hasn't been visited yet, then mark it as visited.
                visited.append(u)
                for e in self.vertices.get(u).edges:
                    queue.append(e)
        
        # Save the result to a file.
        output_file = open('bfs_output.txt', 'w')
        output_file.write(str('BFS path found from node ' + str(v) + ' is: ' + str(visited) + '.'))
        output_file.close()
        return visited

    def dfs(self, v):
        # Perform a Depth-First-Search, that traverses the graph from the vertex v.
        stack = []
        visited = []
        stack.append(v)
        while len(stack) > 0:
            u = stack.pop()
            if u not in visited:
                # If the current vertex hasn't been visited yet, then mark it as visited.
                visited.append(u)
                # Add all edges of the current vertex to the stack.
                for e in self.vertices.get(u).edges:
                    stack.append(e)
        
        # Save the result to a file.
        output_file = open('dfs_output.txt', 'w')
        output_file.write(str('DFS path found from node ' + str(v) + ' is: ' + str(visited) + '.'))
        output_file.close()
        return visited

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
    print('UNWEIGHTED, UNDIRECTED GRAPH TRAVERSAL:')
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
    print('BFS: ' + str(g.bfs(1)))
    print('DFS: ' + str(g.dfs(1)))
    print('-------------------------------------')
