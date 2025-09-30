class Solution:
    def isHappy(self, n: int) -> bool:
        seen=set()
        while n!=1 and n not in seen:
            seen.add(n)
            sum=0
            while n>0:
                x=n%10
                n=n//10
                sum+=x*x
            n=sum
        return n==1
