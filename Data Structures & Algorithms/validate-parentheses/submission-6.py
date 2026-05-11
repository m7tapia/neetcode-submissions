class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for par in s:
            if par in "({[":
                stack.append(par)
            
            elif par in "]})":
                if not stack:
                    return False
                
                popped = stack.pop()

                if not ((par == ")" and popped == "(") 
                    or (par == "}" and popped == "{") 
                    or (par == "]" and popped == "[")):
                    return False

        if stack:
            return False
        else:
            return True
            



            
            




        