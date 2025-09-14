class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l=len(s)-1
        k=0
        for i in range(l,-1,-1):
            if s[i]==" " and k>0:
                break
            if s[i]!=" ":
                k+=1
        return k
