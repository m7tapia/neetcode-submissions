class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #Reverse Polish Notation is you do the numbers first and then the operation
        #So (5 +2) * 4 = 5 2 + 4 *
        

        #Stack works here because we first get numbers then the operation so we pop the last 2 numbers we've seen and do the operation
        #and then we add the result of that operation back to the stack. 
        #We need the stack because it acts as parantheses. Take 5 - (3 + 2) = 5 3 2 + -
        #If we used a queue it would do 5 + 3 = 8 not following our order of operations, then 2 - 8 = -6.
        #But using a stack lets us see the two most recent numbers looked at for an operation which let's 
        #us do the order of operations in the way we want it.

        #In python, floor division // rounds down not to 0. To fix this we can do regular division then cast to an int
        # b/c int does round to 0.
        
        
        
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                second_num = stack.pop()
                first_num = stack.pop()
                stack.append(first_num - second_num)
            elif c == "/":
                second_num = stack.pop()
                first_num = stack.pop()
                stack.append(int(first_num / second_num))
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            else: #it's a number
                stack.append(int(c))

        return stack[0]

        #This is O(n) worst time and O(n) worst space but in reality slightly less than n b/c our list isn't fully numbers and we don't append the arithmetics.


            