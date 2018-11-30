"""
STUDENT NAME: PRANALI DESHMUKH
STUDENT ID: 8923910

UNIT TESTS FOR COURSEWORK ASSIGNMENT 5:

The program for the coursework assignment 5 has been stored with the filename CA_5_Graph_Search.py in the same directory.

Test cases to check the implementation of BFS and DFS traversals for the previous graph structure. The test cases check:
a) the functions addVertex for addition of vertices to the graph, 
b) the function addEdge for addition of edges to the graph,
c) the function bfs for breadth-first-traversal, and 
d) the function dfs for depth-first-traversal

Please Note: I have used Python 2.7 for implementing the program and it's test cases.
"""

import unittest
# Import the Graph class from the file named CA_5_Graph_Search.py.
from CA_5_Graph_Search import Graph

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
        print('TESTING UNWEIGHTED, UNDIRECTED GRAPH TRAVERSAL:')
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


    # Test the bfs method of the Graph.
    def test_bfs(self):
        # Generate graph
        g = Graph()
        # Add nine vertices to the graph.
        for vertex in range(1,10):
            g.addVertex(vertex)
        # Add edges to the graph
        edges = [[1, 9],[9, 7],[9, 3],[7, 6],[7, 8],[8, 5],[1, 2],[3, 6],[3, 5],[3, 4]]
        for edge in edges:
            g.addEdge(edge[0], edge[1])

        # Check if bfs returns the output as [1, 9, 2, 7, 3, 6, 8, 5, 4].
        self.assertEqual(g.bfs(1), [1, 9, 2, 7, 3, 6, 8, 5, 4])
        print('\n-----------------------------------------------')
        print('BFS: ' + str(g.bfs(1)))

        # Check the string output to the bfs_output file.
        bfs_file = open('bfs_output.txt', 'r')
        path = bfs_file.read()
        self.assertEqual('BFS path found from node ' + str(1) + ' is: ' + str(g.bfs(1)) + '.', path)


    # Test the dfs method of the Graph.
    def test_dfs(self):
        # Generate graph
        g = Graph()
        # Add nine vertices to the graph.
        for vertex in range(1,10):
            g.addVertex(vertex)
        # Add edges to the graph
        edges = [[1, 9],[9, 7],[9, 3],[7, 6],[7, 8],[8, 5],[1, 2],[3, 6],[3, 5],[3, 4]]
        for edge in edges:
            g.addEdge(edge[0], edge[1])
        
        # Check if dfs returns the output as [1, 2, 9, 3, 4, 5, 8, 7, 6].
        self.assertEqual(g.dfs(1), [1, 2, 9, 3, 4, 5, 8, 7, 6])
        print('\nDFS: ' + str(g.dfs(1)))
        print('-----------------------------------------------')

        # Check the string output to the dfs_output file.
        dfs_file = open('dfs_output.txt', 'r')
        path = dfs_file.read()
        self.assertEqual('DFS path found from node ' + str(1) + ' is: ' + str(g.dfs(1)) + '.', path)

def main():
    unittest.main()

if __name__ == '__main__':
    main()