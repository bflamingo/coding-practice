def stringReverse(instr):
	reverse = instr[::-1]
	return reverse

def stringReverse_inplace(str_array):
	for i in range(0,int(len(str_array)/2)):
		str_array[i], str_array[-i-1] = str_array[-i-1], str_array[i]
	return str(str_array)

def checkPalindrome(instr):
	isPalindrome = True
	for i in range(0,int(len(instr)/2)):
		print(i)
		if instr[i] != instr[-i-1]:
			isPalindrome = False
			break

	return isPalindrome

def reverseWords(instr):
	word_start = len(instr)-1
	word_end = len(instr)
	reverse = ""
	i = len(instr)-1
	while i >= 0:
		if instr[i] == " ":
			if word_start != word_end:
				reverse += instr[word_start:word_end+1]
				word_end = word_start
			reverse += instr[i]
			if i != 0:
				word_start = i-1
				word_end = i-1
		else:
			if i != 0 and instr[i-1] != " ":
				word_start -= 1

		i -= 1

	if word_start != word_end:
		reverse += instr[word_start:word_end+1]

	return reverse


def reverseWordsEasy(instr):
	words = instr.split(' ')
	return ' '.join(list(reversed(words)))


def reverseWordsHard(instr):
	word_end = len(instr)
	word_start = len(instr)-1
	i = len(instr)-1
	reverse = []
	while i >= 0:
		if instr[i] == ' ':
			reverse.append(instr[i+1:word_end])
			word_end = i
		i -= 1

	if word_end != 0:
		reverse.append(instr[0:word_end])

	return ' '.join(reverse)


def countWords(instr):
	wordcount = {}
	words = instr.split(' ')
	for word in words:
		if word.lower() not in wordcount.keys():
			wordcount[word.lower()] = 1
		else:
			wordcount[word.lower()] += 1

	print(wordcount)


def scanPhoneNumbers(instr):

	

# print(stringReverse("foo bar"))
# print(stringReverse_inplace(list("foo bar")))
# print(checkPalindrome("testset"))
# print(checkPalindrome("testesl"))

# print(reverseWords("test1 test2 test3"))
# print(reverseWordsEasy("test1 test2 test3"))
# print(reverseWordsHard("test1 test2 test3"))

countWords("one Two two three Three Three four Four four four")