class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        
        for c in s:
            if stack: 
                if c.lower() == stack[-1] and c != stack[-1]  or c.upper() == stack[-1]  and  c != stack[-1]:
                    stack.pop()
                else: 
                    stack.append(c)
            else:
                stack.append(c)
        
        return "".join(stack)
