class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 0
        uniq = set()
        for num in nums:
            uniq.add(num)

        for num in uniq:
            if num - 1 not in uniq:
                len = 0
                while num in uniq:
                    num += 1
                    len += 1

                max_len = max(max_len, len)

        return max_len


