"""
STUDENT NAME: PRANALI DESHMUKH
STUDENT ID: 8923910

COURSEWORK ASSIGNMENT 2:

Implement a function that deletes a node in a binary search tree in a language of your choice.

Please Note: I have used Python 2.7 for implementing the program.
"""


class BinaryTreeNode(object):
    # Initialize Binary Tree Node with a value.
    def __init__(self, value):
        print("Inserting value: " + str(value))
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree(object):
    def tree_insert(self, tree, item):
        # Check if this element should be the first/root node in the tree.
        if tree == None:
            tree = BinaryTreeNode(item)
        else:
            # Item should be earlier in the tree than the parent node.
            if(item < tree.value):
                if(tree.left == None):
                    tree.left = BinaryTreeNode(item)
                else:
                    self.tree_insert(tree.left, item)
            # Item should be later in the tree than the parent node.
            else:
                if(tree.right == None):
                    tree.right = BinaryTreeNode(item)
                else:
                    self.tree_insert(tree.right, item)
        return tree


    def in_order(self, tree):
        # Print the left sub-tree, then the current node, and then the right sub-tree.
        if(tree.left != None):
            self.in_order(tree.left)
        print (tree.value)
        if(tree.right != None):
            self.in_order(tree.right)


    def find_min_node(self, tree):
        # If root element is empty then return root.
        if tree == None:
            return tree
        # If root element is not empty then find the node with the minimum value.
        current = tree
        while current.left != None:
            current = current.left
        return current


    def delete_node(self, tree, item):
        # 1st case - tree is empty.
        if tree == None:
            return tree
        # 2nd case - item is less than root.
        elif item < tree.value:
            tree.left = self.delete_node(tree.left, item)
        # 3nd case - item is greater than root.
        elif item > tree.value:
            tree.right = self.delete_node(tree.right, item)
        # 4th case - item is root.
        else:
            # case 4.1 - root has no child.
            if tree.left == None and tree.right == None:
                tree = None
            # case 4.2 - if root has one child.
            elif tree.left == None:
                tree = tree.right
            elif tree.right == None:
                tree = tree.left
            # case 4.3 - if root has 2 child.
            else:
                temp_node = self.find_min_node(tree.right)
                tree.value = temp_node.value
                tree.right = self.delete_node(tree.right, temp_node.value)
        return tree


if __name__ == '__main__':
    
    bst = BinarySearchTree()
    
    binary_tree = None

    print("-------------------------------------------")
    print("BINARY SEARCH TREE:")
    print("-------------------------------------------")

    # Insert values in the tree.
    print("Inserting values within the tree:")
    for item in range(1,8):
        binary_tree = bst.tree_insert(binary_tree, item)

    print("-------------------------------------------")
    # Print the values of the tree in-order.
    print("Tree after insertion of the elements:")
    bst.in_order(binary_tree)

    print("-------------------------------------------")
    # Delete a value from the tree.
    print("Tree after deletion of 3 from it:")
    bst.delete_node(binary_tree, 3)
    bst.in_order(binary_tree)
    print("-------------------------------------------")
