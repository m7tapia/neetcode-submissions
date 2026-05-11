class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        map = {"(": ")", 
               "{": "}", 
               "[": "]"}

        for par in s:
            if par in "({[":
                stack.append(par)
            
            else:
                popped = stack.pop() if stack else "#"
                if not map.get(popped) == par:
                    return False

            
        return not stack




            
            




        