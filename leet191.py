class Solution:
    def hammingWeight(self, n: int) -> int:
        binary = bin(n)[2:]
        bit=0
        for i in binary:
            digit=int(i)
            if digit==1:
                bit+=1
        return bit
