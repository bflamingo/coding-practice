import unittest

## Classes
class Node:
	def __init__(self, data, nextNode=None):
		self.data = data
		self.nextNode = nextNode

	def disp(self):
		print(str(self.data))

	def __eq__(self, other):
		if isinstance(other, self.__class__):
			return (self.data == other.data and self.nextNode == other.nextNode)
		else:
			return False


class DoubleNode:
	def __init__(self, data, nextNode=None, prevNode=None):
		self.data = data
		self.nextNode = nextNode
		self.prevNode = prevNode

	# def __eq__(self, other):
	# 	if isinstance(other, self.__class__):
	# 		return (self.data == other.data and 
	# 			self.nextNode == other.nextNode and 
	# 			self.prevNode == other.prevNode
	# 			)
	# 	else:
	# 		return False


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
		if self.head == None:
			return None
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

	def traverse(self,idx):
		if idx < 0:
			raise ValueError("Index must be a positive integer (incl. 0)")
		if self.head is None:
			raise ValueError("List is empty")

		current_idx = 0
		current_node = self.head

		while current_idx < idx:
			if current_node.nextNode == None:
				raise ValueError("Index out of bounds")
			current_node = current_node.nextNode
			current_idx += 1

		return current_node

	def insert(self, data, idx):
		""" Insert after node in position idx (inserted node is at idx+1). """
		if idx < 0:
			raise ValueError("Index must be a positive integer (incl. 0)")
		if self.head is None:
			if idx == 0:
				self.prepend(Node(data))
				return
			else:
				raise ValueError("Insertion index out of bounds (list is empty)")

		current_node = self.traverse(idx)
		newNode = Node(data)
		newNode.nextNode = current_node.nextNode
		current_node.nextNode = newNode
		return

	def remove(self, idx):
		""" remove node in position idx """
		if idx < 0:
			raise ValueError("Index must be a positive integer (incl. 0)")
		if self.head is None:
			raise ValueError("Cannot remove from empty linked list")
		if self.head.nextNode is None:
			if idx == 0:
				self.head = None
				return
			else:
				raise ValueError("Removal index out of bound (over max index")

		current_node = self.traverse(idx-1)

		## Arrived at node directly before target, need to check
		## that target node exists
		if current_node.nextNode is None:
			raise ValueError("Removal index out of bound (over max index)")

		delete_node = current_node.nextNode
		new_next = current_node.nextNode.nextNode
		current_node.nextNode = new_next
		delete_node = None

		return

	def reverseInPlace(self, left, right):
		""" Reverse contiguous chunk of a linked list

			Inputs:
			left - index of the beginning position of sublist to reverse
			right - index of the end position of sublist to reverse
		"""

		if left > right:
			raise ValueError("Left index should not exceed right index.")
		if left == right:
			return
		if self.head is None:
			return
		if left < 0 or right < 0:
			raise ValueError("Indices should be nonnegative integers")





		
class DoublyLinkedList:
	def __init__(self):
		self.head = None
		self.tail = None

	def append(self, data):
		if self.head == None and self.tail == None:
			self.head = DoubleNode(data)
			self.tail = self.head
		else:
			newTail = DoubleNode(data, None, self.tail)
			self.tail.nextNode = newTail
			self.tail = newTail

	def prepend(self, data):
		if self.head == None and self.tail == None:
			self.head = DoubleNode(data)
			self.tail = self.head
		else:
			newHead = DoubleNode(data, self.head, None)
			self.head.prevNode = newHead
			self.head = newHead

	def popTail(self):
		if self.tail == None:
			return None

		popped = self.tail
		self.tail = self.tail.prevNode

		if self.tail == None:
			self.head = self.tail
		else:
			self.tail.nextNode = None
		return popped

	def popHead(self):
		if self.head == None:
			return None

		popped = self.head
		self.head = self.head.nextNode

		if self.head == None:
			self.tail = self.head
		else:
			self.head.prevNode = None
		return popped

	def insert(self, data, idx):
		""" Insert after node in position idx (inserted node is at idx+1). """
		if idx < 0:
			raise ValueError("Index must be a positive integer (incl. 0)")
		if self.head is None:
			if idx == 0:
				self.prepend(data)
				return
			else:
				raise ValueError("Insertion index out of bounds (list is empty)")

		current_idx = 0
		current_node = self.head

		while current_idx < idx:
			if current_node.nextNode is None:
				raise ValueError("Insertion index out of bound (over max index)")
			current_node = current_node.nextNode
			current_idx += 1

		if current_node == self.tail:
			self.append(data)
			return

		## Do the insertion (lol)
		newNode = DoubleNode(data, current_node.nextNode, current_node)
		current_node.nextNode.prevNode = newNode
		current_node.nextNode = newNode
		return

	def remove(self, idx):
		""" remove node in position idx """
		if idx < 0:
			raise ValueError("Index must be a positive integer (incl. 0)")
		if self.head is None:
			raise ValueError("Cannot remove from empty linked list")
		if self.head.nextNode is None:
			if idx == 0:
				self.head = None
				self.tail = None
				return
			else:
				raise ValueError("Removal index out of bound (over max index")

		current_idx = 0
		current_node = self.head

		while current_idx < idx-1:
			if current_node.nextNode is None:
				raise ValueError("Removal index out of bound (over max index)")
			current_node = current_node.nextNode
			current_idx += 1

		## Arrived at node directly before target, need to check
		## that target node exists
		if current_node.nextNode is None:
			raise ValueError("Removal index out of bound (over max index)")

		delete_node = current_node.nextNode
		
		if current_node.nextNode == self.tail:
			current_node.nextNode = None
			self.tail = current_node
			delete_node = None
		else:
			new_next = current_node.nextNode.nextNode
			new_next.prevNode = current_node
			current_node.nextNode = new_next
			delete_node = None

		return


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

	def test_insert_ListIsEmptyAndIndexIsZero(self):
		self.llist.insert(1,0)

		self.assertEqual(self.llist.head.data, Node(1))

	def test_insert_ListIsEmptyAndIndexIsInvalid(self):
		inserted = True
		try:
			self.llist.insert(1,1)
		except ValueError:
			inserted = False

		self.assertFalse(inserted)

	def test_insert_InsertBetweenTwoNodes(self):
		self.llist.append(1)
		self.llist.append(3)
		self.llist.insert(2,0)

		self.assertEqual(self.llist.head.data, 1)
		self.assertEqual(self.llist.head.nextNode.data, 2)
		self.assertEqual(self.llist.head.nextNode.nextNode.data, 3)

	def test_insert_NonemptyListIndexOutOfBounds(self):
		self.llist.append(0)
		self.llist.append(1)

		inserted = True
		try:
			self.llist.insert(2,2)
		except ValueError:
			inserted = False

		self.assertFalse(inserted)

	def test_insert_NonemptyListInsertAtTail(self):
		self.llist.append(0)
		self.llist.append(1)
		self.llist.append(2)

		self.llist.insert(3,2)

		self.assertEqual(self.llist.head.data, 0)
		self.assertEqual(self.llist.head.nextNode.data, 1)
		self.assertEqual(self.llist.head.nextNode.nextNode.data, 2)
		self.assertEqual(self.llist.head.nextNode.nextNode.nextNode.data, 3)

	def test_insert_NegativeIndexError(self):
		try:
			self.llist.insert(0,-1)
		except ValueError:
			return

		self.fail()

	def test_remove_EmptyListThrowsException(self):
		deleted = True
		try:
			self.llist.remove(0)
		except ValueError:
			deleted = False

		self.assertFalse(deleted)

	def test_remove_NonEmptyListIndexOutOfBounds(self):
		deleted = True
		self.llist.append(0)
		self.llist.append(1)

		try:
			self.llist.remove(2)
		except ValueError:
			deleted = False

		self.assertFalse(deleted)
		self.assertEqual(self.llist.head.data, 0)
		self.assertEqual(self.llist.head.nextNode.data, 1)

	def test_remove_JustHead(self):
		self.llist.append(0)
		self.llist.remove(0)

		self.assertEqual(self.llist.head, None)

	def test_remove_NegativeIndex(self):
		self.llist.append(0)
		self.llist.append(1)

		removed = True
		try:
			self.llist.remove(-1)
		except ValueError:
			removed = False

		self.assertFalse(removed)

	def test_remove_LastNode(self):
		self.llist.append(0)
		self.llist.append(1)
		self.llist.append(2)

		self.llist.remove(2)

		self.assertEqual(self.llist.head.data, 0)
		self.assertEqual(self.llist.head.nextNode.data, 1)
		self.assertEqual(self.llist.head.nextNode.nextNode, None)

	def test_remove_MiddleNode(self):
		self.llist.append('A')
		self.llist.append('B')
		self.llist.append('C')

		self.llist.remove(1)

		self.assertEqual(self.llist.head.data, 'A')
		self.assertEqual(self.llist.head.nextNode.data, 'C')
		self.assertEqual(self.llist.head.nextNode.nextNode, None)


class TestDoublyLinkedList(unittest.TestCase):

	def setUp(self):
		self.llist = DoublyLinkedList()

	def test_prepend_empty(self):
		self.llist.prepend('test')
		self.assertEqual(self.llist.head.data, 'test')
		self.assertEqual(self.llist.head.nextNode, None)
		self.assertEqual(self.llist.head.prevNode, None)

		self.assertEqual(self.llist.tail.data, 'test')
		self.assertEqual(self.llist.tail.nextNode, None)
		self.assertEqual(self.llist.tail.prevNode, None)

	def test_prepend_nonempty_1(self):
		self.llist.prepend(1)
		self.llist.prepend(2)

		self.assertEqual(self.llist.head.prevNode, None)
		self.assertEqual(self.llist.head.data, 2)
		self.assertEqual(self.llist.head.nextNode.data, 1)

		self.assertEqual(self.llist.tail.nextNode, None)
		self.assertEqual(self.llist.tail.data, 1)
		self.assertEqual(self.llist.tail.prevNode.data, 2)

	def test_prepend_nonempty_2(self):
		self.llist.prepend(1)
		self.llist.prepend(2)
		self.llist.prepend(3)

		self.assertEqual(self.llist.head.prevNode, None)
		self.assertEqual(self.llist.head.data, 3)
		self.assertEqual(self.llist.head.nextNode.data, 2)
		self.assertEqual(self.llist.head.nextNode.nextNode.data, 1)

		self.assertEqual(self.llist.tail.nextNode, None)
		self.assertEqual(self.llist.tail.data, 1)
		self.assertEqual(self.llist.tail.prevNode.data, 2)
		self.assertEqual(self.llist.tail.prevNode.prevNode.data, 3)
		
	def test_append_empty(self):
		self.llist.append('test')
		self.assertEqual(self.llist.head.data, 'test')
		self.assertEqual(self.llist.head.nextNode, None)
		self.assertEqual(self.llist.head.prevNode, None)

		self.assertEqual(self.llist.tail.data, 'test')
		self.assertEqual(self.llist.tail.nextNode, None)
		self.assertEqual(self.llist.tail.prevNode, None)

	def test_append_nonempty_1(self):
		self.llist.append(1)
		self.llist.append(2)

		self.assertEqual(self.llist.head.prevNode, None)
		self.assertEqual(self.llist.head.data, 1)
		self.assertEqual(self.llist.head.nextNode.data, 2)

		self.assertEqual(self.llist.tail.nextNode, None)
		self.assertEqual(self.llist.tail.data, 2)
		self.assertEqual(self.llist.tail.prevNode.data, 1)

	def test_append_nonempty_2(self):
		self.llist.append(1)
		self.llist.append(2)
		self.llist.append(3)

		self.assertEqual(self.llist.head.prevNode, None)
		self.assertEqual(self.llist.head.data, 1)
		self.assertEqual(self.llist.head.nextNode.data, 2)
		self.assertEqual(self.llist.head.nextNode.nextNode.data, 3)

		self.assertEqual(self.llist.tail.nextNode, None)
		self.assertEqual(self.llist.tail.data, 3)
		self.assertEqual(self.llist.tail.prevNode.data, 2)
		self.assertEqual(self.llist.tail.prevNode.prevNode.data, 1)

	def test_popHead_justHead(self):
		self.llist.append(1)
		poppedHead = self.llist.popHead()

		self.assertEqual(poppedHead.data, 1)
		self.assertEqual(self.llist.head, None)
		self.assertEqual(self.llist.tail, None)

	def test_popHead_twoNodes(self):
		self.llist.append(1)
		self.llist.append(2)

		poppedHead = self.llist.popHead()

		self.assertEqual(poppedHead.data, 1)
		
		self.assertEqual(self.llist.head.data, 2)
		self.assertEqual(self.llist.head.nextNode, None)
		self.assertEqual(self.llist.head.prevNode, None)

		self.assertEqual(self.llist.tail.data, 2)
		self.assertEqual(self.llist.tail.nextNode, None)
		self.assertEqual(self.llist.tail.prevNode, None)

	def test_popHead_threeNodes(self):
		self.llist.append(1)
		self.llist.append(2)
		self.llist.append(3)

		poppedHead = self.llist.popHead()

		self.assertEqual(poppedHead.data, 1)

		self.assertEqual(self.llist.head.prevNode, None)
		self.assertEqual(self.llist.head.data, 2)
		self.assertEqual(self.llist.head.nextNode.data, 3)

		self.assertEqual(self.llist.tail.nextNode, None)
		self.assertEqual(self.llist.tail.data, 3)
		self.assertEqual(self.llist.tail.prevNode.data, 2)

	def test_popTail_justHead(self):
		self.llist.append(1)
		poppedTail = self.llist.popTail()

		self.assertEqual(poppedTail.data, 1)
		self.assertEqual(self.llist.head, None)
		self.assertEqual(self.llist.tail, None)

	def test_popTail_twoNodes(self):
		self.llist.append(1)
		self.llist.append(2)

		poppedTail = self.llist.popTail()

		self.assertEqual(poppedTail.data, 2)

		self.assertEqual(self.llist.head.data, 1)
		self.assertEqual(self.llist.head.nextNode, None)
		self.assertEqual(self.llist.head.prevNode, None)

		self.assertEqual(self.llist.tail.data, 1)
		self.assertEqual(self.llist.tail.nextNode, None)
		self.assertEqual(self.llist.tail.prevNode, None)

	def test_popTail_threeNodes(self):
		self.llist.append(1)
		self.llist.append(2)
		self.llist.append(3)

		poppedTail = self.llist.popTail()

		self.assertEqual(poppedTail.data, 3)

		self.assertEqual(self.llist.head.prevNode, None)
		self.assertEqual(self.llist.head.data, 1)
		self.assertEqual(self.llist.head.nextNode.data, 2)

		self.assertEqual(self.llist.tail.nextNode, None)
		self.assertEqual(self.llist.tail.data, 2)
		self.assertEqual(self.llist.tail.prevNode.data, 1)

	def test_insert_ListIsEmptyAndIndexIsZero(self):
		self.llist.insert(1,0)

		self.assertEqual(self.llist.head.data, 1)
		self.assertEqual(self.llist.head.nextNode, None)
		self.assertEqual(self.llist.head.prevNode, None)

		self.assertEqual(self.llist.tail.data, 1)
		self.assertEqual(self.llist.tail.nextNode, None)
		self.assertEqual(self.llist.tail.prevNode, None)

	def test_insert_ListIsEmptyAndIndexIsInvalid(self):
		inserted = True
		try:
			self.llist.insert(1,1)
		except ValueError:
			inserted = False

		self.assertFalse(inserted)

	def test_insert_InsertBetweenTwoNodes(self):
		self.llist.append(1)
		self.llist.append(3)
		self.llist.insert(2,0)

		self.assertEqual(self.llist.head.prevNode, None)
		self.assertEqual(self.llist.head.data, 1)
		self.assertEqual(self.llist.head.nextNode.data, 2)
		self.assertEqual(self.llist.head.nextNode.nextNode.data, 3)

		self.assertEqual(self.llist.tail.nextNode, None)
		self.assertEqual(self.llist.tail.data, 3)
		self.assertEqual(self.llist.tail.prevNode.data, 2)
		self.assertEqual(self.llist.tail.prevNode.prevNode.data, 1)

	def test_insert_NonemptyListIndexOutOfBounds(self):
		self.llist.append(0)
		self.llist.append(1)

		inserted = True
		try:
			self.llist.insert(2,2)
		except ValueError:
			inserted = False

		self.assertFalse(inserted)

	def test_insert_NonemptyListInsertAtTail(self):
		self.llist.append(0)
		self.llist.append(1)
		self.llist.append(2)

		self.llist.insert(3,2)

		self.assertEqual(self.llist.head.prevNode, None)
		self.assertEqual(self.llist.head.data, 0)
		self.assertEqual(self.llist.head.nextNode.data, 1)
		self.assertEqual(self.llist.head.nextNode.nextNode.data, 2)
		self.assertEqual(self.llist.head.nextNode.nextNode.nextNode.data, 3)

		self.assertEqual(self.llist.tail.nextNode, None)
		self.assertEqual(self.llist.tail.data, 3)
		self.assertEqual(self.llist.tail.prevNode.data, 2)
		self.assertEqual(self.llist.tail.prevNode.prevNode.data, 1)
		self.assertEqual(self.llist.tail.prevNode.prevNode.prevNode.data, 0)

	def test_insert_NegativeIndexError(self):
		try:
			self.llist.insert(0,-1)
		except ValueError:
			return

		self.fail()

	def test_remove_EmptyListThrowsException(self):
		deleted = True
		try:
			self.llist.remove(0)
		except ValueError:
			deleted = False

		self.assertFalse(deleted)

	def test_remove_NonEmptyListIndexOutOfBounds(self):
		deleted = True
		self.llist.append(0)
		self.llist.append(1)

		try:
			self.llist.remove(2)
		except ValueError:
			deleted = False

		self.assertFalse(deleted)
		self.assertEqual(self.llist.head.data, 0)
		self.assertEqual(self.llist.head.nextNode.data, 1)

	def test_remove_JustHead(self):
		self.llist.append(0)
		self.llist.remove(0)

		self.assertEqual(self.llist.head, None)
		self.assertEqual(self.llist.tail, None)

	def test_remove_NegativeIndex(self):
		self.llist.append(0)
		self.llist.append(1)

		removed = True
		try:
			self.llist.remove(-1)
		except ValueError:
			removed = False

		self.assertFalse(removed)

	def test_remove_LastNode(self):
		self.llist.append(0)
		self.llist.append(1)
		self.llist.append(2)

		self.llist.remove(2)

		self.assertEqual(self.llist.head.prevNode, None)
		self.assertEqual(self.llist.head.data, 0)
		self.assertEqual(self.llist.head.nextNode.data, 1)

		self.assertEqual(self.llist.tail.nextNode, None)
		self.assertEqual(self.llist.tail.data, 1)
		self.assertEqual(self.llist.tail.prevNode.data, 0)

	def test_remove_MiddleNode(self):
		self.llist.append('A')
		self.llist.append('B')
		self.llist.append('C')

		self.llist.remove(1)

		self.assertEqual(self.llist.head.prevNode, None)
		self.assertEqual(self.llist.head.data, 'A')
		self.assertEqual(self.llist.head.nextNode.data, 'C')

		self.assertEqual(self.llist.tail.nextNode, None)
		self.assertEqual(self.llist.tail.data, 'C')
		self.assertEqual(self.llist.tail.prevNode.data, 'A')


if __name__ == '__main__':
	suite1 = unittest.TestLoader().loadTestsFromTestCase(TestLinkedList)
	suite2 = unittest.TestLoader().loadTestsFromTestCase(TestDoublyLinkedList)
	suite = unittest.TestSuite([suite1, suite2])
	#suite = suite1
	# suite = unittest.TestSuite()
	# suite.addTest(TestDoublyLinkedList('test_append_nonempty_1'))
	runner = unittest.TextTestRunner(verbosity=2)
	runner.run(suite)

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