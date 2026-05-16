class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        max_count = 0
        for num in nums:
            if num - 1 not in s:
                count = 0
                while num in s:
                    count += 1
                    num += 1
                if count > max_count:
                    max_count = count

        return max_count