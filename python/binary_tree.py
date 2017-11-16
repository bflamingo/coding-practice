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


class BinarySearchTree(object):
    def __init__(self,value):
        self.root = None


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
        



if __name__ == '__main__':
    unittest.main(verbosity=2)