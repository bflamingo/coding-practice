import re
import unittest

def matchPhoneNumbers(instr):
    match_phones = r'\(?\d{3}\)?[ .-]?\d{3}[ .-]?\d{4}'
    pattern = re.compile(match_phones)
    phone_nums = []
    
    nums = pattern.finditer(instr)
    for num in nums:
        if num.group() not in phone_nums:
            phone_nums.append(num.group())
    
    return phone_nums


class Test_matchPhoneNumbers(unittest.TestCase):
    
    def test_ThreePhoneNumbers(self):
        testnums = '(123)456-7890  123.456.7890  123 456 7890'
        testnums_list = ['(123)456-7890', '123.456.7890', '123 456 7890']
        checknums = matchPhoneNumbers(testnums)
        
        for num in checknums:
            self.assertTrue(num in testnums_list)


if __name__ == '__main__':
	unittest.main(verbosity=2)