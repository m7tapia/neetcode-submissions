from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #this is the better O(n) time solution
        #Uses a Deque
        #key idea: if we append a new number that is bigger and younger than numbers in front of it,
        #then we popleft the numbers behind it b/c they will never be the max again. However we can,
        #append smaller numbers b/c even tho they're smaller we still need to keep them around b/c they
        #may become the max when the older numbers go out of range of our window.
        dq = deque()
        res = []
        l = 0

        for r in range(len(nums)):
            if dq:
                while dq and dq[0][0] < l:
                    #if old numbers in dq are out of the window pop them
                    dq.popleft()

                while dq and dq[-1][1] < nums[r]:
                    dq.pop()
                    #if our new number is greater than old numbers, pop those off 

            dq.append((r, nums[r]))

            if r - l + 1 == k:
                res.append(dq[0][1])
                l += 1

        return res





