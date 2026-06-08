class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #Reverse Polish Notation is you do the numbers first and then the operation
        #So (5 +2) * 4 = 5 2 + 4 *
        
        #Also note: that python always rounds down not towards 0 but we can get around this
        stack = []
        for i in tokens:
            if i == "+":
                stack.append(stack.pop() + stack.pop())
            elif i == "-":
                second_num = stack.pop()
                first_num = stack.pop()
                stack.append(first_num - second_num)
            elif i == "/":
                second_num = stack.pop()
                first_num = stack.pop()
                stack.append(int(first_num / second_num))
            elif i == "*":
                stack.append(stack.pop() * stack.pop())
            else: #it's a number
                stack.append(int(i))

        return stack.pop()


            