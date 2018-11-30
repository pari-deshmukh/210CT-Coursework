"""
STUDENT NAME: PRANALI DESHMUKH
STUDENT ID: 8923910

UNIT TESTS FOR COURSEWORK ASSIGNMENT 1:

The program for the coursework assignment 1 has been stored with the filename CA_1_BST.py in the same directory.

The test cases here check the following output from the Binary Search Tree program:
a) Preorder output of the Binary Search Tree:
     i] Preordered Alphabetically
    ii] Preordered by Frequency.
b) Finding a word:
     i] When the search-word is present
    ii] When the search-word is absent.

Please Note: I have used Python 2.7 for implementing the program and it's test cases.
"""

import unittest
# Import the BinarySearchTree class from the file named CA_1_BST.py.
from CA_1_BST import BinarySearchTree

class TestBST(unittest.TestCase):
    # Test the output printed when the Tree is preordered alphabetically.
    def test_preorder_alphabetically(self):
        bst = BinarySearchTree()
        t = bst.create_tree('Alphabet')
        print("\nAlphabetically Preordered Tree:-")
        bst.preorder(t)

    # Test the output printed when the Tree is preordered by the frequency of words.
    def test_preorder_by_frequency(self):
        bst = BinarySearchTree()
        t = bst.create_tree('Frequency')
        print("\nFrequency Wise Preordered Tree:-")
        bst.preorder(t)

    # Test the search output when the Tree is preordered alphabetically.
    def test_search_word_tA(self):
        bst = BinarySearchTree()
        t = bst.create_tree('Alphabet')
        print(bst.search_word(t, 'the'))
        print(bst.search_word(t, 'was'))

    # Test the search output when the Tree is preordered by the frequency of words.
    def test_search_word_tF(self):
        bst = BinarySearchTree()
        t = bst.create_tree('Frequency')
        print(bst.search_word(t, 'the'))
        print(bst.search_word(t, 'was'))


def main():
    unittest.main()

if __name__ == '__main__':
    main()