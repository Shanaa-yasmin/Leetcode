class Solution:
    def isPalindrome(self, s: str) -> bool:
        words=s.lower()
        x=""
        for i in words:
	        if i.isalnum():
		        x+=i
        l=len(x)-1
        for i in range(0,len(x)//2):
            if x[i]!=x[l]:
                return False
            l-=1
        return True
	
	
