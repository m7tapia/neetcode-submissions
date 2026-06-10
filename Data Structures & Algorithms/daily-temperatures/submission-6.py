class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #brute force is just to do a nested loop

        #a better way is to use a monotonic decreasing stack
        #we append to our stack and whenever we append a temp that's greater than the previous ones,
        #first we pop all the ones that are less than it. So we always have a monotonic decreasing stack.
        #When we pop we subtract the new temp index with the popped index and that's what we append 
        #to our result array for the index of the popped. When we're done iterating through the list, 
        #the temps that are still in the stack don't have a temp greater than them.

        stack, res = [], [-100] * len(temperatures)  

        for i, temp in enumerate(temperatures):
            #if the temp is greater than the min of the stack; keep on popping there's nothing less than temp left than append
            while stack and temp > stack[-1][1]:
                popped = stack.pop()
                res[popped[0]] = i - popped[0]
            stack.append((i, temp))

        #handle temps that didn't have one greater
        while stack:
            popped = stack.pop()
            res[popped[0]] = 0

        return res

        #This is O(n) time b/c we the outer loop iterates n times and the inner loop can iterate 
        #at most n times b/c it depends on stack not being empty and each iteration of the while loop
        #we pop and we can pop at most n times before running out of temps. So O(2n) = O(n)

        #and O(n) space complexity


