class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for par in s:
            #if its an opening just append it to the stack
            if par in "({[":
                stack.append(par)
            
            #if its a closing
            elif par in "]})":
                #if stack is empty there's no opening for this closing paranthesis
                if not stack:
                    return False
                
                #pop the last opening paranthesis from the stack
                popped = stack.pop()

                #return False if the opening and closing paranthesis don't match
                if not ((par == ")" and popped == "(") 
                    or (par == "}" and popped == "{") 
                    or (par == "]" and popped == "[")):
                    return False

        #now just check if the stack is empty and there are no opening paranthesis that 
        #didn't have a partner
        if stack:
            return False
        else:
            return True
            



            
            




        