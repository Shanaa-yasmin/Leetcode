class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number=0
        for d in digits:
	        number=number*10+d
        number=number+1
        digits.clear()
        digits = [int(d) for d in str(number)]
        return digits
