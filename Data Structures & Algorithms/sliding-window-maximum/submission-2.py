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
