from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #this is the better O(n) time solution
        #Uses a Deque
        #Intuiton: 
        #We want our deque to hold decreasing numbers from left to right. 
        #This is called a monotonic deque (a deque we maintained order either increasing or decreasing).
        #When we append to the end (right), we check if there are older numbers (left) that are smaller.
        #If there are, that means that the new number is bigger and younger, so we will never need those older
        #numbers again. So we pop from the right until we get rid of those smaller older numbers and then append.
        #If our new number is smaller, we append b/c rn its not the max but when the bigger numbers are out of the window
        #it may be the max. We also make sure to pop old numbers from the left that are no 
        #longer in our window. 
        #Maintaining our deque like this makes sure the current max number at the front (left) of our
        #deque is always the max in our window.
        dq = deque()
        res = []
        l = 0

        for r in range(len(nums)):
            if dq:
                #make sure if we're trying to access it, that there IS something to access (while dq)
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

        #Runtime is O(n) b/c we can only append n times and there are 2 ways a number can be removed,
        #either popleft() when its out of the window or pop() when we don't need it anymore.
        #Each number can only get removed once.
        #Total work: O(n [each append] + n [each pop]) = O(2n) = O(n)

        #Space complexity is O(k) where k is the size of the window since we pop elements once they're out of the window.







