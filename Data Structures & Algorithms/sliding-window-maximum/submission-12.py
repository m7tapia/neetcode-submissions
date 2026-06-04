from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #this is the better O(n) time solution
        #Uses a Deque
        #key idea: 
        #We want our deque to hold decreasing numbers from left to right.
        #When we append to to end (right), we check if there are older numbers (left) that are smaller.
        #If there are, that means that the new number is bigger and younger, so we will never need those older
        #numbers again. So we pop from the right until we get rid of those smaller older numbers and then append.
        #If our new number is smaller, we append b/c rn its not the max but when the bigger numbers are out of the window
        #it may be the max. 
        dq = deque()
        res = []
        l = 0

        for r in range(len(nums)):
            if dq:
                

                while dq and dq[-1][1] < nums[r]:
                    dq.pop()
                    #if our new number is greater than old numbers, pop those off.
                    #We pop starting the end (right) of the deque since our deque is decreasing

                while dq and dq[0][0] < l:
                    #if old numbers in dq are out of the window pop them
                    dq.popleft()
            dq.append((r, nums[r]))

            if r - l + 1 == k:
                res.append(dq[0][1])
                l += 1

        return res





