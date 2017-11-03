import re
import unittest

def countDuplicateWords(instr):
	pattern = re.compile(r'\b\w*\b')
	words = pattern.finditer(instr)

	wordcount = {}

	for word in words:
		found = word.group().lower()
		if found not in wordcount.keys():
			wordcount[found] = 1
		else:
			wordcount[found] += 1

	return wordcount


def countDuplicateWords_file(file):
	pattern = re.compile(r'\b\w*\b')
	wordcount = {}

	with open(file) as f:

		for line in f:
			words = pattern.finditer(line)
			for word in words:
				found = word.group().lower()

				if found not in wordcount.keys():
					wordcount[found] = 1
				else:
					wordcount[found] += 1

	return wordcount

def matchPhoneNumbers(str):
	pattern = re.compile(r'\(?\d{3}\)?[ .-]?\d{3}[ .-]?\d{4}$')
	phone_numbers = []

	numbers = pattern.finditer()
	for number in numbers:
		



class TestRegex(unittest.TestCase):

	def test_CountDuplicateWords_TwoOfEach(self):
		check = "Two two of Of Each each"
		countDict = countDuplicateWords(check)
		
		self.assertTrue('two' in countDict.keys())
		self.assertTrue('of' in countDict.keys())
		self.assertTrue('each' in countDict.keys())

		self.assertEqual(countDict['two'], 2)
		self.assertEqual(countDict['of'], 2)
		self.assertEqual(countDict['each'], 2)

	def test_countDuplicateWords_file_TwoOfEach(self):
		file = "testdata/test_countDuplicateWords_file_TwoOfEach.txt"
		countDict = countDuplicateWords_file(file)

		self.assertTrue('two' in countDict.keys())
		self.assertTrue('of' in countDict.keys())
		self.assertTrue('each' in countDict.keys())

		self.assertEqual(countDict['two'], 2)
		self.assertEqual(countDict['of'], 2)
		self.assertEqual(countDict['each'], 2)


if __name__ == "__main__":
	unittest.main(verbosity=2)