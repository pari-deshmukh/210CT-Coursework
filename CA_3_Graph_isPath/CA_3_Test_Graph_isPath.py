"""
STUDENT NAME: PRANALI DESHMUKH
STUDENT ID: 8923910

UNIT TESTS FOR COURSEWORK ASSIGNMENT 3:

The program for the coursework assignment 3 has been stored with the filename CA_3_Graph_isPath.py in the same directory.

Test cases to check the implementation of an unweighted, undirected graph containing positive integers. The test cases check:
a) the functions addVertex for addition of vertices to the graph, 
b) the function addEdge for addition of edges to the graph, and 
c) the function isPath by passing two vertices to it and then checking if there is a path between the two nodes. 

Please Note: I have used Python 2.7 for implementing the program and it's test cases.
"""

import unittest
# Import the Graph class from the file named CA_3_Graph_isPath.py.
from CA_3_Graph_isPath import Graph

class TestGraph(unittest.TestCase):

    # Test the addVertex method of the graph.
    def test_addVertex(self):

        # Generate graph
        g = Graph()

        # Add nine vertices to the graph.
        for vertex in range(1,10):
            g.addVertex(vertex)

        # Check if there are 9 vertices in the tree.
        self.assertEqual(len(g.vertices),9)


    # Test the addEdge method of the graph.
    def test_addEdge(self):

        # Generate graph
        g = Graph()

        # Add nine vertices to the graph.
        for vertex in range(1,10):
            g.addVertex(vertex)

        # Add ten edges to the graph
        edges = [[1, 9],[9, 7],[9, 3],[7, 6],[7, 8],[8, 5],[1, 2],[3, 6],[3, 5],[3, 4]]
        
        for edge in edges:
            g.addEdge(edge[0], edge[1])

        print('-----------------------------------------------')
        print('TESTING UNWEIGHTED, UNDIRECTED GRAPH:')
        print('-----------------------------------------------')

        # Print the Graph's vertices.
        print('Vertices: ' + str(g.vertices.keys()))

        # Print all the edges for each vertex in the graph.
        print('\nEdges:')
        
        # Initialize the edgeCounter to zero
        edgeCount = 0
        for vertex in range(1,10):
            print('\nEdges from vertex "' + str(vertex) +'": ')
            for e in g.vertices.get(vertex).edges:
                # Increment edge counter by 1 for every linked vertex. At the end the edgeCount should be equal to twenty since each edge is connected to two vertices.
                edgeCount += 1
                print('[' + str(vertex) + '-' + str(e) +']')

        # Check if the number of edges in the tree is equal to the number of edges input.
        self.assertEqual(edgeCount/2,len(edges))


    # Test the isPath method of the Graph.
    def test_isPath(self):
        # Generate graph
        g = Graph()
        # Add nine vertices to the graph.
        for vertex in range(1,10):
            g.addVertex(vertex)
        # Add edges to the graph
        edges = [[1, 9],[9, 7],[9, 3],[7, 6],[7, 8],[8, 5],[1, 2],[3, 6],[3, 5],[3, 4]]
        for edge in edges:
            g.addEdge(edge[0], edge[1])

        # Check if isPath returns True when v=1 and w=5.
        self.assertTrue(g.isPath(1, 5))

        print('\n-----------------------------------------------')
        print('isPath(1, 5): ' + str(g.isPath(1, 5)))
        print('-----------------------------------------------')

        # Check the string output to the path file.
        path_file = open('path.txt', 'r')
        path = path_file.read()
        self.assertEqual('Path found from node 1 to node 5 is: [1, 9, 3, 5].', path)


def main():
    unittest.main()

if __name__ == '__main__':
    main()