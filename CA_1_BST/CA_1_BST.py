"""
STUDENT NAME: PRANALI DESHMUKH
STUDENT ID: 8923910

COURSEWORK ASSIGNMENT 1:

Build a Binary Search Tree (BST) to hold English language words in its nodes. Use a paragraph of any text in order to extract words and to determine their frequencies.
Input: You should read the paragraph from a suitable file format, such as .txt. 
The following tree operations should be implemented: 
a) Printing the tree in pre-order. 
b) Finding a word.
Regardless whether found or not found your program should output the path traversed in determining the answer, followed by yes if found or no, respectively.

Note: The assignment does not specify how the tree is supposed to look. As such, I assume that the node labels are words, while frequencies are additional values for them.
As per this assumption, I have written 2 different methods to insert nodes into the tree:
a) Nodes sorted in alphabetical order
b) Nodes sorted by their corresponding frequencies.

Please Note: I have used Python 2.7 for implementing the program.
"""


class BinaryTreeNode(object):
    # Initialize Binary Tree Node with the given word and it's frequency.
    def __init__(self, word, frequency):
        self.word = word
        self.frequency = frequency
        self.left = None
        self.right = None


class BinarySearchTree(object):
    def read_input_paragraph(self):
        # Read a text file named paragraph
        input_file = open('paragraph.txt', 'r')
        text = input_file.read()

        # Check if the paragraph is empty
        if not text:
            print("The paragraph is empty")
            quit()

        # Remove all commas, question marks and fullstops from the text.
        text = text.replace(",", "")
        text = text.replace(".", "")
        text = text.replace("?", "")

        # Define an empty dictionary for storing the Words as Keys and the corresponding Frequencies as Values.
        frequencies_dict = {}

        # Populate the dictionary with words the words and their corresponding frequencies.
        for word in text.split():
            if word not in frequencies_dict:
                frequencies_dict[word] = 1
            else:
                frequencies_dict[word] += 1
        
        return frequencies_dict

    
    def create_tree(self, sort_type):
        # Define an empty tree, which would be filled up with the words and frequencies from the input text.
        binary_tree = None

        frequencies_dict = self.read_input_paragraph()

        # Create the tree from the frequencies dictionary sorted by sort order type specified
        for key, value in frequencies_dict.items():    
            if binary_tree == None:
                binary_tree = self.tree_insert(None, key, value, sort_type)
            else:
                self.tree_insert(binary_tree, key, value, sort_type)

        return binary_tree

    def tree_insert(self, tree, word, frequency, sort_type):
        # Check if this element should be the first/root node in the tree.
        if tree == None:
            tree = BinaryTreeNode(word, frequency)
        else:
            if sort_type == 'Alphabet':
                # Word should be earlier in alphabetical order than the parent node.
                if(word < tree.word):
                    if(tree.left == None):
                        tree.left = BinaryTreeNode(word, frequency)
                    else:
                        self.tree_insert(tree.left, word, frequency, sort_type)
                # Word should be later in alphabetical order than the parent node.
                else:
                    if(tree.right == None):
                        tree.right = BinaryTreeNode(word, frequency)
                    else:
                        self.tree_insert(tree.right, word, frequency, sort_type)

            elif sort_type == 'Frequency':
                # Word's frequency is less than the parent node.
                if(frequency < tree.frequency):
                    if(tree.left == None):
                        tree.left = BinaryTreeNode(word, frequency)
                    else:
                        self.tree_insert(tree.left, word, frequency, sort_type)
                # Word's frequency is not less than the parent node.
                else:
                    if(tree.right == None):
                        tree.right = BinaryTreeNode(word, frequency)
                    else:
                        self.tree_insert(tree.right, word, frequency, sort_type)

            else:
                print("Incorrect Sort Type!")
                quit()
        return tree


    def preorder(self, tree):
        # Return the current node, then follow the left sub-tree, and then the right sub-tree.
        print("Word: '" + tree.word + "', Frequency: " + str(tree.frequency))
        if(tree.left != None):
            self.preorder(tree.left)
        if(tree.right != None):
            self.preorder(tree.right)


    def search_word(self, tree, word):
        # Navigate the given tree to find the given word.
        print("\nSearching for the word: '" + word +
            "'\n-------------------------------------------")
        while tree != None:
            print("Current word: '" + tree.word +
                "', Frequency: " + str(tree.frequency))
            if tree.word == word:
                return "-------------------------------------------\nYes! \nThe word '" + word + "' was found!"
            elif tree.word > word:
                # Looking earlier in the alphabetical order (left sub-tree).
                tree = tree.left
            else:
                # Looking further in the alphabetical order (right sub-tree).
                tree = tree.right
        return "-------------------------------------------\nNo! \nThe word '" + word + "' was not found!"


if __name__ == "__main__":

    bst = BinarySearchTree()

    tF = bst.create_tree('Frequency')
    print("-------------------------------------------")
    print("BINARY SEARCH TREE:")
    print("-------------------------------------------")
    print("Frequency Wise Preordered Tree:-")
    bst.preorder(tF)

    print(bst.search_word(tF, 'the'))
    print(bst.search_word(tF, 'was'))

    tA = bst.create_tree('Alphabet')
    print("\nAlphabetically Preordered Tree:-")
    bst.preorder(tA)

    print(bst.search_word(tA, 'the'))
    print(bst.search_word(tA, 'was'))
