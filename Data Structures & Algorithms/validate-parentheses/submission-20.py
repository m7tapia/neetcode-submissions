class Solution:
    def isValid(self, s: str) -> bool:
        #we use a stack, if its an opening paranthesis we push it to the stack
        #if its closing we pop an opened one. if when we pop the stack is empty that means 
        #there's no opening paranthesis for that closing one.
        #else if the popped opening paranthesis doesn't correspond with the closing one 
        #the paranthesis aren't valid b/c they don't go together.
        #if we end and the stack isn't empty, that means there's too many opening paranthesis.
        #otherwise everything is valid.
        stack = []
        pairs = {"}": "{", "]": "[", ")": "("}
        
        for par in s:
            if par in pairs.values(): #if par is an opening paranthesis
                stack.append(par)
            else: #if par is a closing paranthesis
                if not stack: 
                    return False
                popped = stack.pop() #popped is the opening paranthesis that should go with par
                if popped != pairs[par]: 
                    return False

        return not stack

        #O(n) time and O(n) space
