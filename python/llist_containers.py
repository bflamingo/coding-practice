import llist
import unittest

class LListStack:
	def __init__(self):
		self.linklist = llist.LinkedList()

	def push(self, data):
		self.linklist.prepend(data)
		return None

	def pop(self):
		if self.linklist.head is None:
			return None
		else:
			return self.linklist.popHead().data

	def peek(self):
		if self.linklist.head is None:
			return None
		else:
			return self.linklist.head.data


class DLListQueue:
	def __init__(self):
		self.dlinklist = llist.DoublyLinkedList()

	def enqueue(self, data):
		self.dlinklist.append(data)
		return None

	def dequeue(self):
		if self.dlinklist.head is None:
			return None
		else:
			return self.dlinklist.popHead().data

	def peek(self):
		if self.dlinklist.head is None:
			return None
		else:
			return self.dlinklist.head.data


class StackQueue:
	def __init__(self):
		self.stack1 = LListStack()
		self.stack2 = LListStack()

	def enqueue(self, data):
		self.stack1.push(data)
		return None

	def dequeue(self):
		if self.stack1.peek() is None:
			return None
		else:
			while self.stack1.peek() is not None:
				self.stack2.push(self.stack1.pop())
			retval = self.stack2.pop()

			while self.stack2.peek() is not None:
				self.stack1.push(self.stack2.pop())

			return retval

	def peek(self):
		if self.stack1.peek() is None:
			return None
		else:
			while self.stack1.peek() is not None:
				self.stack2.push(self.stack1.pop())
			retval = self.stack2.peek()

			while self.stack2.peek() is not None:
				self.stack1.push(self.stack2.pop())

			return retval


class TestLListStack(unittest.TestCase):
	def setUp(self):
		self.stack = LListStack()

	def test_CheckPushedItemsUsingPeek(self):
		self.stack.push('1')
		self.assertEqual(self.stack.peek(), '1')

		self.stack.push(2)
		self.assertEqual(self.stack.peek(), 2)

		self.stack.push(3.0)
		self.assertEqual(self.stack.peek(), 3.0)

	def test_PushThreeItemsThenPop(self):
		self.stack.push(1)
		self.stack.push(2)
		self.stack.push(3)

		self.assertEqual(self.stack.pop(), 3)
		self.assertEqual(self.stack.pop(), 2)
		self.assertEqual(self.stack.pop(), 1)

	def test_PushAfterPopping(self):
		self.stack.push(1)
		self.stack.push(2)

		self.assertEqual(self.stack.peek(), 2)
		self.assertEqual(self.stack.pop(), 2)
		self.assertEqual(self.stack.peek(), 1)

		self.stack.push(3)

		self.assertEqual(self.stack.peek(), 3)
		self.assertEqual(self.stack.pop(), 3)
		self.assertEqual(self.stack.peek(), 1)
		self.assertEqual(self.stack.pop(), 1)

	def test_PopEmptyStack(self):
		self.assertEqual(self.stack.pop(), None)

	def test_PeekEmptyStack(self):
		self.assertEqual(self.stack.peek(), None)


class TestStackQueue(unittest.TestCase):
	def setUp(self):
		self.mqueue = StackQueue()

	def test_CheckEnqueueUsingPeek(self):
		# Queue is FIFO, so first added item should stay as the peek value.
		self.mqueue.enqueue('1')
		self.assertEqual(self.mqueue.peek(), '1')

		self.mqueue.enqueue(2)
		self.assertEqual(self.mqueue.peek(), '1')

		self.mqueue.enqueue(3.0)
		self.assertEqual(self.mqueue.peek(), '1')

	def test_EnqueueAndDequeue(self):
		self.mqueue.enqueue('1')
		self.mqueue.enqueue(2)
		self.mqueue.enqueue(3.0)

		self.assertEqual(self.mqueue.dequeue(), '1')
		self.assertEqual(self.mqueue.dequeue(), 2)
		self.assertEqual(self.mqueue.dequeue(), 3.0)
		self.assertEqual(self.mqueue.dequeue(), None)


class TestDLListQueue(TestStackQueue):
	def setUp(self):
		self.mqueue = DLListQueue()


if __name__ == '__main__':
	# suite = unittest.TestLoader().loadTestsFromTestCase(TestLListStack)
	suite = unittest.TestLoader().loadTestsFromTestCase(TestDLListQueue)
	# suite = unittest.TestSuite([suite1, suite2])
	# suite = suite1
	# suite = unittest.TestSuite()
	# suite.addTest(TestDoublyLinkedList('test_append_nonempty_1'))
	runner = unittest.TextTestRunner(verbosity=2)
	runner.run(suite)