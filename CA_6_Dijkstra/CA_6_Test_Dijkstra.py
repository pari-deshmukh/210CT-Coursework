"""
STUDENT NAME: PRANALI DESHMUKH
STUDENT ID: 8923910

UNIT TESTS FOR COURSEWORK ASSIGNMENT 6:

The program for the coursework assignment 6 has been stored with the filename CA_6_Dijkstra.py in the same directory.

Test cases to check the implementation of Dijkstra's algorithm on weighted connections for the previous graph structure. The test cases check:
a) the functions addVertex for addition of vertices to the graph, 
b) the function addEdge for addition of edges to the graph, and 
d) the function dijkstra for dijkstra's output.

Please Note: I have used Python 2.7 for implementing the program and it's test cases.
"""

import unittest
# Import the Graph class from the file named CA_6_Dijkstra.py.
from CA_6_Dijkstra import Graph

class TestGraph(unittest.TestCase):

    # Test the addVertex method of the graph.
    def test_addVertex(self):

        # Generate graph
        g = Graph()

        # Add vertices to the graph.
        for vertex in map(chr,range(ord('A'),ord('H')+1)):
            g.addVertex(vertex)
        g.addVertex('S')

        # Check if there are 9 vertices in the tree.
        self.assertEqual(len(g.vertices),9)


    # Test the addEdge method of the graph.
    def test_addEdge(self):

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

        print('-----------------------------------------------')
        print('TESTING WEIGHTED GRAPH:')
        print('-----------------------------------------------')

        # Print the Graph's vertices.
        print('Vertices: ' + str(g.vertices.keys()))

        # Print all the edges for each vertex.
        print('\nEdges:')
        for vertex in map(chr,range(ord('A'),ord('H')+1)):
            print('\nEdges from vertex "' + vertex +'": ')
            for e in g.vertices.get(vertex).edges:
                print('[' + vertex + '-' + str(e) +'] -> ' + str(g.vertices.get(vertex).edges[e]))

        # Check if the number of edges in the tree is equal to the number of edges input, i.e. 10.
        self.assertEqual(len(edges),10)


    # Test the bfs method of the Graph.
    def test_bfs(self):
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
        
        # Check if the dijkstra method returns the output as 10 for the source node 'A' and destination node 'E'.
        self.assertEqual(g.dijkstra('A', 'E'), 10)
        print('\n-----------------------------------------------')
        print("Dijkstra's output: " + str(g.dijkstra('A', 'E')))
        print('-----------------------------------------------')

def main():
    unittest.main()

if __name__ == '__main__':
    main()