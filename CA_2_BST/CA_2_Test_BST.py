"""
STUDENT NAME: PRANALI DESHMUKH
STUDENT ID: 8923910

UNIT TEST FOR COURSEWORK ASSIGNMENT 2:

The program for the coursework assignment 2 has been stored with the filename CA_2_BST.py in the same directory.

The test cases here check the output before and after the deletion of a node from the Binary Search Tree program to check the implementation of the delete_node function. It also has implicitly coverage of the tree_insert, in_order and find_min_node functions of the BinarySearchTree class as the tree_insert function is invoked while inserting nodes within the tree, while the in_order function if invoked while printing the tree. The find_min_node function is invoked implicitly while executing the delete_node function.

Please Note: I have used Python 2.7 for implementing the program and it's test cases.
"""

import unittest
# Import the BinarySearchTree class from the file named CA_2_BST.py.
from CA_2_BST import BinarySearchTree

class TestBST(unittest.TestCase):
    # Test the node deletion function of the Binary Search Tree.
    def test_delete_node(self):
        bst = BinarySearchTree()
        binary_tree = None

        print("-------------------------------------------")
        print("TESTING BINARY SEARCH TREE NODE DELETION:")
        print("-------------------------------------------")

        # Insert values in the tree using the tree_insert function of the BinarySearchTree class.
        print("Inserting values within the tree:")
        for item in range(1,8):
            binary_tree = bst.tree_insert(binary_tree, item)

        print("-------------------------------------------")
        # Print the values of the tree in-order function of the BinarySearchTree class.
        print("Tree after insertion of the elements:")
        bst.in_order(binary_tree)

        print("-------------------------------------------")
        # Delete a value from the tree delete_node function of the BinarySearchTree class.
        print("Tree after deletion of 3 from it:")
        bst.delete_node(binary_tree, 3)
        bst.in_order(binary_tree)
        print("-------------------------------------------")

def main():
    unittest.main()

if __name__ == '__main__':
    main()