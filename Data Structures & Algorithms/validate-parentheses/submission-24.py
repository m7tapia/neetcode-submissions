class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {'(': ')', '{': '}', '[': ']'}

        for char in s:
            if char in pairs.keys():
                stack.append(char)

            else:
                if not stack:
                    return False
                popped = stack.pop()
                if pairs[popped] != char:
                    return False

        return not stack