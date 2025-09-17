class Solution:
    def romanToInt(self, s: str) -> int:
        val={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        intgr=0
        i=0
        while i<len(s):
            if i+1<len(s) and val[s[i]]<val[s[i+1]]:
                intgr+=val[s[i+1]]-val[s[i]]
                i+=2
            else:
                intgr+=val[s[i]]
                i+=1
        return intgr
        
