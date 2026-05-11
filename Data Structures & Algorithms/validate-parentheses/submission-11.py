class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        map = {"(": ")", 
               "{": "}", 
               "[": "]"}

        for par in s:
            #if par is opening just append it to stack
            if par in "({[":
                stack.append(par)
            #if par is closing
            else:
                #pop if stack is not empty, if it is assign popped something random
                popped = stack.pop() if stack else "#"

                #if popped == #, map.get(popped) will be None which != to par
                if not map.get(popped) == par:
                    #if popped and par don't correspond return False
                    return False

        #if stack is not empty return False
        return not stack




            
            




        