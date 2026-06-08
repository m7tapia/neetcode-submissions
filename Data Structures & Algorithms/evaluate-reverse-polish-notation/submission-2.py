class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #Reverse Polish Notation is you do the numbers first and then the operation
        #So (5 +2) * 4 = 5 2 + 4 *
        #Also note: that python always rounds down not towards 0 but we can get around this by converting it to an int which rounds it to 0.

        #Stack works here because we first get numbers then the operation so we pop our last numbers and do the operation
        #and then we add the result of that operation back to the stack. 
        #There are no edge cases here, if we get to an arithmetic character then our stack will always have 2 numbers.
        
        #We need the stack because it acts as parantheses. Take 5 - (3 + 2) = 5 3 2 + -
        #If we used a queue it would do 5 + 3 = 8, then 2 - 8 = -6 which messes up our order of operations. 
        #But using a stack lets us see the two most recent numbers looked at for an operation which let's 
        #us do the order of operations in the way we want it.
        
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


            