class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #brute force is just to do a nested loop

        #a better way is to use a monotonic decreasing stack
        #we append to our stack and whenever we append a temp that's greater than the previous ones,
        #we pop the ones that are less than it. So we always have a monotonic decreasing stack.
        #When we pop we subtract the new temp index with the popped index and that's what we append 
        #to our result array for the index of the popped. When we're done iterating through the list, 
        #the temps that are still in the stack don't have a temp greater than them after them.

        stack, res = [], [-100] * len(temperatures)  

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                popped = stack.pop()
                res[popped[0]] = i - popped[0]
            stack.append((i, temp))

        #handle temps that didn't have one greater
        while stack:
            popped = stack.pop()
            res[popped[0]] = 0

        return res


