import re

def findPhoneNum(instr):
    phone_regex = r'1?[ .-]?\(?\d{3}\)?[ .-]?\d{3}[ .-]?\d{4}'
    match = re.compile(phone_regex)
    phonenums = match.findall(instr)
    return phonenums

nums = findPhoneNum('1-408-123-4568 4081234568 408.123.4568')
for num in nums:
	print(nums)


# \(?\d{3}\)?[ .-]?\d{3}[ .-]?\d{4}

# match one instance of string:

# \b(?!\w*foo\w*foo\w*)\w*foo\w*\b

# import re

# def findPhoneNum(instr):
#     phone_regex = r'1?[ .-]?\(?\d{3}\)?[ .-]?\d{3}[ .-]?\d{4}'
#     match = re.compile(phone_regex)
#     phonenums = match.findall(instr)
#     return phonenums

# def findPhoneNumFile(filename):
#     pattern = re.compile(r'1?[ .-]?\(?\d{3}\)?[ .-]?\d{3}[ .-]?\d{4}')
#     with open(filename) as f:
#         for line in f:
#             matches = pattern.finditer(line)
#             for num in matches:
#                 phone_numbers.append(num)