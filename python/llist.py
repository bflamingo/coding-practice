import unittest

## Classes
class Node:
	def __init__(self, data, nextNode = None):
		self.data = data
		self.nextNode = nextNode

	def disp(self):
		print(str(self.data))

	def __eq__(self, other):
		if isinstance(other, self.__class__):
			return (self.data == other.data and self.nextNode == other.nextNode)
		else:
			return False


class LinkedList:
	def __init__(self):
		self.head = None

	def prepend(self, data):
		newHead = Node(data, self.head)
		self.head = newHead

	def append(self, data):
		if self.head is None:
			self.prepend(data)
		
		else:
			following = self.head
			while following.nextNode is not None:
				following = following.nextNode

			following.nextNode = Node(data)

	def popHead(self):
		popped = self.head
		self.head = self.head.nextNode
		return popped

	def popTail(self):
		penult = self.head
		if self.head.nextNode is None:
			self.head = None
			return penult

		while penult.nextNode.nextNode is not None:
			penult = penult.nextNode

		popped = penult.nextNode
		penult.nextNode = None
		return popped

	def traverse(self, idx):
		following = self.head
		






## Unit tests
class TestLinkedList(unittest.TestCase):

	def setUp(self):
		self.llist = LinkedList()

	def test_prepend_empty(self):
		self.llist.prepend('test')
		self.assertEqual(self.llist.head.data, 'test')
		self.assertEqual(self.llist.head.nextNode, None)

	def test_prepend_nonempty_1(self):
		self.llist.prepend(1)
		tempNode = Node(self.llist.head.data, self.llist.head.nextNode)

		self.llist.prepend(2)
		self.assertEqual(self.llist.head.data, 2)
		# self.assertEqual(self.llist.head.nextNode.data, tempNode.data)
		# self.assertEqual(self.llist.head.nextNode.nextNode, tempNode.nextNode)
		self.assertEqual(self.llist.head.nextNode, tempNode)

	def test_prepend_nonempty_2(self):
		self.llist.prepend(1)
		self.llist.prepend(2)

		tempNode = Node(self.llist.head.data, self.llist.head.nextNode)

		self.llist.prepend(3)

		self.assertEqual(self.llist.head.data, 3)
		self.assertEqual(self.llist.head.nextNode, tempNode)

	def test_append_empty(self):
		self.llist.append('test')
		self.assertEqual(self.llist.head, Node('test'))

	def test_append_nonempty_1(self):
		self.llist.append(1)
		self.llist.append(2)

		checkTail = Node(2)
		checkHead = Node(1,checkTail)

		self.assertEqual(self.llist.head, checkHead)
		self.assertEqual(self.llist.head.nextNode, checkTail)

	def test_popHead_justHead(self):
		self.llist.append(1)
		poppedHead = self.llist.popHead()

		self.assertEqual(poppedHead, Node(1))
		self.assertEqual(self.llist.head, None)

	def test_popHead_twoNodes(self):
		self.llist.append(1)
		self.llist.append(2)

		poppedHead = self.llist.popHead()

		self.assertEqual(poppedHead.data, 1)
		self.assertEqual(self.llist.head, Node(2))

	def test_popHead_threeNodes(self):
		self.llist.append(1)
		self.llist.append(2)
		self.llist.append(3)

		poppedHead = self.llist.popHead()

		self.assertEqual(poppedHead.data, 1)
		self.assertEqual(self.llist.head, Node(2,Node(3)))

	def test_popTail_justHead(self):
		self.llist.append(1)
		poppedTail = self.llist.popTail()

		self.assertEqual(poppedTail, Node(1))
		self.assertEqual(self.llist.head, None)

	def test_popTail_twoNodes(self):
		self.llist.append(1)
		self.llist.append(2)

		poppedTail = self.llist.popTail()

		self.assertEqual(poppedTail.data, 2)
		self.assertEqual(self.llist.head, Node(1))

	def test_popTail_threeNodes(self):
		self.llist.append(1)
		self.llist.append(2)
		self.llist.append(3)

		poppedTail = self.llist.popTail()

		self.assertEqual(poppedTail.data, 3)
		self.assertEqual(self.llist.head, Node(1,Node(2)))



if __name__ == '__main__':
	unittest.main(verbosity=2)

# llist = LinkedList()
# llist.prepend(1)
# llist.prepend(2)
# llist.append(3)
# llist.prepend(4)
# llist.append(5)

# following = llist.head
# while following is not None:
# 	following.disp()
# 	following = following.nextNode