class Solution:
    def isValid(self, s: str) -> bool:
        sym={')':'(','}':'{',']':'['}
        stack=[]
        for i in s:
            if i=='(' or i=='{' or i=='[':
                stack.append(i)
            elif i==')' or i=='}' or i==']':
                if not stack:
                    return False
                else:
                    x=stack.pop()
                    if x!=sym[i]:
                        return False
        return not stack
