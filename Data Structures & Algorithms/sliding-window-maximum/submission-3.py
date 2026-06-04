class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        l, r = 0, k - 1

        while r < len(nums):
            max_num = float('-inf')
            for i in range(l, r + 1):
                num = nums[i]
                max_num = max(max_num, num)
            
            res.append(max_num)
            r += 1
            l += 1

        return res


    #this is what I was able to come up with by myself
    #this is the brute force approach. 
    #let n = total # of elements in nums, k = size of the window

    #you find the number of windows by using n - k + 1 ~ n - k

    # k is the number of operations per window

    #so the runtime is O((n - k) * k) and ofc extra space complexity is O(1) since res array doesnt count

    #this represents the number of windows times the work done in each window


    #note we found the formula for # of windows n - k + 1 by either counting
    #or seeing that you start at index zero and you have a window that takes up k elements, 
    #so the remaining number of elements to your right of the window is n - k.
    #Each time you shift forward for a new window, you go forward once. Those are your next windows, 
    #and you have to add one for the first window, your starting window. 

#Say your array has n = 7 elements and your window size is k = 3.
#1. Place the first window at the start. It covers three elements.
#2. Look at how many elements are left over on the right. 7 - 3 = 4 elements.
#3. Because there are four elements left, you can slide the window to the right exactly four times before hitting the wall.
#Total windows = 1 (start) + 4 (shifts) = 5 windows.



    