import unittest

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


def findMaxDepthDFS(root):
	max_depth = 0
	current_depth = -1
	s = []
	s.append(root)
	while s:
		start_size = len(s) ## increase depth if size remains or increases, decrease if decreases
		current = s.pop()
		current_depth += 1
		
		if current_depth > max_depth:
			max_depth = current_depth
		
		if current.right is not None:
			s.append(current.right)
		
		if current.left is not None:
			s.append(current.left)
		
		if len(s) < start_size:
			current_depth -= 1

	return max_depth




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



if __name__ == '__main__':
	unittest.main(verbosity=2)