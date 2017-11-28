import unittest
from collections import deque

class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def addLeft(self, new_value):
        self.left = TreeNode(new_value)

    def addRight(self, new_value):
        self.right = TreeNode(new_value)

    def __eq__(self,other):
        if not isinstance(other, self.__class__):
            return False

        return(
            (self.value == other.value) and 
            (self.left == other.left) and 
            (self.right == other.right)
            )


class BSTNode:
    def __init__(self, key, value):
        self.key = key
        self.value = [value]
        self.left = None
        self.right = None

    def addLeft(self, key, value):
        self.left = BSTNode(key, value)

    def addRight(self, key, value):
        self.right = BSTNode(key, value)


class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def insert(self, key, value):
        if self.root is None:
            self.root = BSTNode(key, value)

        else:
            parent = None
            current = self.root
            while current is not None:
                if key == current.key:
                    current.value.append(value)
                    return
                elif key > current.key:
                    parent, current = current, current.right
                    if current is None:
                        #parent.right = BSTNode(key, value)
                        parent.addRight(key, value)
                else: # key < current.key
                    parent, current = current, current.left
                    if current is None:
                        #parent.left = BSTNode(key, value)
                        parent.addLeft(key, value)
        return None

    def search(self, key):
        current = self.root

        while current is not None:
            if key == current.key:
                return current
            elif key > current.key:
                current = current.right
            else: # key < current.key
                current = current.left

        return None

    def find_max(self, node):
        """ Maximum node in a subtree is the right-most node,
            so we can iteratively traverse the right subtree
            until we reach the end.
        """
        current_node = node
        while current_node.right:
            current_node = current_node.right
        return current_node

    def remove(self, key):
        ## Search for parent of node to delete
        current_node = self.root
        parent_node = None
        while (current_node.key != key) and current_node is not None:
            if key > current_node.key:
                parent_node, current_node = current_node, current_node.right
            else: # key < current_node.key
                parent_node, current_node = current_node, current_node.left
        if current_node is None:
            return None # Key not present, nothing to remove.

        if current_node.left and current_node.right:
            in_order_pred = self.find_max(current_node.left)
            temp_key,temp_val = in_order_pred.key, in_order_pred.value
            self.remove(in_order_pred.key)
            current_node.key, current_node.value = temp_key, temp_val
        elif current_node.left:
            if current_node is parent_node.left:
                parent_node.left = current_node.left
            else:
                parent_node.right = current_node.left
        elif current_node.right:
            if current_node is parent_node.left:
                parent_node.left = current_node.right
            else:
                parent_node.right = current_node.right
        else: # is a leaf
            if parent_node is None:
                self.root = None
            else:
                if current_node is parent_node.left:
                    parent_node.left = None
                else:
                    parent_node.right = None

        return None


def findMaxDepthDFS(root, s=None):
    """ First attempt to find max depth non-recursively.
    
        Doesn't actually work though. BFS should be better.
    """
    max_depth = -1 ## initialize, since root depth will be 0.
    s = []
    s.append(root)
    current_path = []
    while s:
        current = s.pop()
        current_path.append(current)
        print([node.value for node in current_path])
        
        ## if leaf, check current depth against max, then go back up.
        if current.right is None and current.left is None:
            if len(current_path)-1 > max_depth:
                max_depth = len(current_path)-1
            current_path.pop()

        else:
            if current.right is not None:
                s.append(current.right)

            if current.left is not None:
                s.append(current.left)
        
    return max_depth

def findMaxDepthBFS(root):
    """ Non-recursive algorithm to find the max depth of a binary tree.

        Algorithm works by traversing the tree with BFS, and converting it
        to its implicit data structure representation as an array. Based
        on the length of the array, we can determine the height using the
        fact that the height of a full binary tree is 2**(h+1) - 1, and that
        there are 2**h nodes in each level. This lets us compute a window of
        all indices in a level, which we can use in reverse to find the depth
        of a node given its index.
    """

    to_visit = deque()
    arrayify = []
    to_visit.append(root)

    while to_visit:
        current_node = to_visit.popleft()
        arrayify.append(current_node.value)
        




class TestTreeNode(unittest.TestCase):

    def test_CreateATreeNode(self):
        node = TreeNode(0)
        self.assertEqual(node.value, 0)
        self.assertEqual(node.left, None)
        self.assertEqual(node.right, None)

    def test_AddLeftNode(self):
        root = TreeNode(0)
        root.addLeft(1)

        # Check root
        self.assertEqual(root.value, 0)
        self.assertEqual(root.left, TreeNode(1))
        self.assertEqual(root.right, None)

        # Check left
        self.assertEqual(root.left.value, 1)
        self.assertEqual(root.left.left, None)
        self.assertEqual(root.left.right, None)

    def test_AddRightNode(self):
        root = TreeNode(0)
        root.addRight(1)

        # Check root
        self.assertEqual(root.value, 0)
        self.assertEqual(root.left, None)
        self.assertEqual(root.right, TreeNode(1))

        # Check left
        self.assertEqual(root.right.value, 1)
        self.assertEqual(root.right.left, None)
        self.assertEqual(root.right.right, None)

    def test_MaxDepthWithOnlyRoot(self):
        root = TreeNode(0)
        self.assertEqual(findMaxDepthDFS(root),0)

    def test_MaxDepth_OneLongBranch(self):
        root = TreeNode(0)
        root.left = TreeNode(1)
        root.left.left = TreeNode(2)
        root.left.left.left = TreeNode(3)

        self.assertEqual(findMaxDepthDFS(root),3)

    def test_MaxDepth_SimpleTree(self):
        """Simple tree, see diagram here for how tree looks.
        
                            0
                          /   \
                         1     5
                        / \     \
                       2   3     6
                            \
                             4
        """

        root = TreeNode(0)
        root.addLeft(1)
        root.addRight(5)
        root.left.addLeft(2)
        root.left.addRight(3)
        root.left.right.addRight(4)
        root.right.addRight(6)

        self.assertEqual(findMaxDepthDFS(root),3)
        

class TestBST(unittest.TestCase):
    def setUp(self):
        self.bst = BinarySearchTree()

    def test_insert_NoDuplicates(self):
        """ Use insert to build basic BST.
        Diagram:
                    10
                    /\
                   /  \
                  /    \
                 5      20
                / \    /  \
               3   7  15  25
                     / 
                    14
        """

        self.bst.insert(10,1)
        self.bst.insert(5,2)
        self.bst.insert(20,3)
        self.bst.insert(3,4)
        self.bst.insert(7,5)
        self.bst.insert(15,6)
        self.bst.insert(14,7)
        self.bst.insert(25,8)

        self.assertEqual(self.bst.root.key, 10)
        self.assertEqual(self.bst.root.value, [1])

        # left subtree
        self.assertEqual(self.bst.root.left.key, 5)
        self.assertEqual(self.bst.root.left.value, [2])

        self.assertEqual(self.bst.root.left.left.key, 3)
        self.assertEqual(self.bst.root.left.left.value, [4])

        self.assertEqual(self.bst.root.left.right.key, 7)
        self.assertEqual(self.bst.root.left.right.value, [5])

        # right subtree
        self.assertEqual(self.bst.root.right.key, 20)
        self.assertEqual(self.bst.root.right.value, [3])

        self.assertEqual(self.bst.root.right.left.key, 15)
        self.assertEqual(self.bst.root.right.left.value, [6])

        self.assertEqual(self.bst.root.right.left.left.key, 14)
        self.assertEqual(self.bst.root.right.left.left.value, [7])

        self.assertEqual(self.bst.root.right.right.key, 25)
        self.assertEqual(self.bst.root.right.right.value, [8])

    def test_insert_WithDuplicates(self):
        """ Use insert to build basic BST with duplicate key insertions.
        Diagram:
                    10
                    /\
                   /  \
                  /    \
                 5      20
                / \    /  \
               3   7  15  25
                     / 
                    14
        """

        self.bst.insert(10,1)
        self.bst.insert(10,2)
        
        self.bst.insert(5,2)
        
        self.bst.insert(20,3)
        self.bst.insert(20,4)
        
        self.bst.insert(3,4)
        self.bst.insert(7,5)
        self.bst.insert(15,6)
        self.bst.insert(14,7)
        self.bst.insert(25,8)

        self.bst.insert(5,123)
        self.bst.insert(14,456)

        self.assertEqual(self.bst.root.key, 10)
        self.assertEqual(self.bst.root.value, [1,2])

        # left subtree
        self.assertEqual(self.bst.root.left.key, 5)
        self.assertEqual(self.bst.root.left.value, [2,123])

        self.assertEqual(self.bst.root.left.left.key, 3)
        self.assertEqual(self.bst.root.left.left.value, [4])

        self.assertEqual(self.bst.root.left.right.key, 7)
        self.assertEqual(self.bst.root.left.right.value, [5])

        # right subtree
        self.assertEqual(self.bst.root.right.key, 20)
        self.assertEqual(self.bst.root.right.value, [3,4])

        self.assertEqual(self.bst.root.right.left.key, 15)
        self.assertEqual(self.bst.root.right.left.value, [6])

        self.assertEqual(self.bst.root.right.left.left.key, 14)
        self.assertEqual(self.bst.root.right.left.left.value, [7,456])

        self.assertEqual(self.bst.root.right.right.key, 25)
        self.assertEqual(self.bst.root.right.right.value, [8])

    def test_remove_NoDuplicates(self):
        """ Use insert to build basic BST, then remove some nodes.
        Diagram before removal:
                    10
                    /\
                   /  \
                  /    \
                 5      20
                / \    /  \
               3   7  15  25
                     / 
                    14
        Step 1 remove (root):
                    7
                    /\
                   /  \
                  /    \
                 5      20
                /      /  \
               3      15  25
                     / 
                    14
        Step 2 remove (two children):
                     7
                    /\
                   /  \
                  /    \
                 5      15
                /      /  \
               3      14  25
        Step 3 remove (one child,left):
                     7
                    /\
                   /  \
                  /    \
                 3      15
                       /  \
                      14  25
        Step 4 remove (leaf):
                     7
                    /\
                   /  \
                  /    \
                 3      15
                          \
                          25
        Step 5 remove (one child, right):
                     7
                    /\
                   /  \
                  /    \
                 3      25
        Step 6: Remove til empty
        """

        self.bst.insert(10,1)
        self.bst.insert(5,2)
        self.bst.insert(20,3)
        self.bst.insert(3,4)
        self.bst.insert(7,5)
        self.bst.insert(15,6)
        self.bst.insert(14,7)
        self.bst.insert(25,8)

        ############################################################
        # Step 1
        ############################################################
        self.bst.remove(10)

        self.assertEqual(self.bst.root.key, 7)
        self.assertEqual(self.bst.root.value, [5])

        # left subtree
        self.assertEqual(self.bst.root.left.key, 5)
        self.assertEqual(self.bst.root.left.value, [2])

        self.assertEqual(self.bst.root.left.left.key, 3)
        self.assertEqual(self.bst.root.left.left.value, [4])

        self.assertEqual(self.bst.root.left.right, None)

        # right subtree
        self.assertEqual(self.bst.root.right.key, 20)
        self.assertEqual(self.bst.root.right.value, [3])

        self.assertEqual(self.bst.root.right.left.key, 15)
        self.assertEqual(self.bst.root.right.left.value, [6])

        self.assertEqual(self.bst.root.right.left.left.key, 14)
        self.assertEqual(self.bst.root.right.left.left.value, [7])

        self.assertEqual(self.bst.root.right.right.key, 25)
        self.assertEqual(self.bst.root.right.right.value, [8])


        ############################################################
        # Step 2
        ############################################################
        self.bst.remove(20)

        self.assertEqual(self.bst.root.key, 7)
        self.assertEqual(self.bst.root.value, [5])

        # left subtree
        self.assertEqual(self.bst.root.left.key, 5)
        self.assertEqual(self.bst.root.left.value, [2])

        self.assertEqual(self.bst.root.left.left.key, 3)
        self.assertEqual(self.bst.root.left.left.value, [4])

        self.assertEqual(self.bst.root.left.right, None)

        # right subtree
        self.assertEqual(self.bst.root.right.key, 15)
        self.assertEqual(self.bst.root.right.value, [6])

        self.assertEqual(self.bst.root.right.left.key, 14)
        self.assertEqual(self.bst.root.right.left.value, [7])

        self.assertEqual(self.bst.root.right.left.left, None)

        self.assertEqual(self.bst.root.right.right.key, 25)
        self.assertEqual(self.bst.root.right.right.value, [8])


        ############################################################
        # Step 3
        ############################################################
        self.bst.remove(5)

        self.assertEqual(self.bst.root.key, 7)
        self.assertEqual(self.bst.root.value, [5])

        # left subtree
        self.assertEqual(self.bst.root.left.key, 3)
        self.assertEqual(self.bst.root.left.value, [4])

        self.assertEqual(self.bst.root.left.left, None)

        self.assertEqual(self.bst.root.left.right, None)

        # right subtree
        self.assertEqual(self.bst.root.right.key, 15)
        self.assertEqual(self.bst.root.right.value, [6])

        self.assertEqual(self.bst.root.right.left.key, 14)
        self.assertEqual(self.bst.root.right.left.value, [7])

        self.assertEqual(self.bst.root.right.right.key, 25)
        self.assertEqual(self.bst.root.right.right.value, [8])


        ############################################################
        # Step 4
        ############################################################
        self.bst.remove(14)

        self.assertEqual(self.bst.root.key, 7)
        self.assertEqual(self.bst.root.value, [5])

        # left subtree
        self.assertEqual(self.bst.root.left.key, 3)
        self.assertEqual(self.bst.root.left.value, [4])

        # right subtree
        self.assertEqual(self.bst.root.right.key, 15)
        self.assertEqual(self.bst.root.right.value, [6])

        self.assertEqual(self.bst.root.right.left, None)

        self.assertEqual(self.bst.root.right.right.key, 25)
        self.assertEqual(self.bst.root.right.right.value, [8])


        ############################################################
        # Step 5
        ############################################################
        self.bst.remove(15)

        self.assertEqual(self.bst.root.key, 7)
        self.assertEqual(self.bst.root.value, [5])

        # left subtree
        self.assertEqual(self.bst.root.left.key, 3)
        self.assertEqual(self.bst.root.left.value, [4])

        # right subtree
        self.assertEqual(self.bst.root.right.key, 25)
        self.assertEqual(self.bst.root.right.value, [8])

        self.assertEqual(self.bst.root.right.right, None)


        ############################################################
        # Step 6
        ############################################################
        self.bst.remove(3)
        self.bst.remove(25)

        self.assertEqual(self.bst.root.key, 7)
        self.assertEqual(self.bst.root.value, [5])

        # left subtree
        self.assertEqual(self.bst.root.left, None)

        # right subtree
        self.assertEqual(self.bst.root.right, None)

        self.bst.remove(7)

        self.assertEqual(self.bst.root, None)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestBST)
    # suite = unittest.TestSuite([suite1, suite2])
    # suite = suite1
    # suite = unittest.TestSuite()
    # suite.addTest(TestDoublyLinkedList('test_append_nonempty_1'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)