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

    #you find the number of windows by using n - k + 1 ~ n - k
    #we find this by starting our first window. it'll cover the first k elements and then we can only slide our window
    #forward by one index n - k times after that. If you want to be precise you can add the 1 for the first window 
    #but it doesn't rlly change much so we drop it.

    # k is the number of operations per window

    #so the runtime is O((n - k) * k) and ofc extra space complexity is O(1) since res array doesnt count

    #this represents the number of windows times the work done in each window

    #we do a lot of repeated checks in this approach


