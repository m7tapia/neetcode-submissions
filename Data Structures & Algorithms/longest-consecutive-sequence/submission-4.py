class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniq_nums = set(nums)

        arr = []
        for num in uniq_nums:
            arr.append(num)

        arr.sort()

        if len(arr) == 0:
            return 0

        count, top_count, = 1, 1

        for i, num in enumerate(arr):
            if i == 0:
                continue
            if arr[i] == arr[i-1] + 1:
                count += 1

            else:
                if top_count < count:
                    top_count = count
                count = 1

        return top_count if top_count > count else count
            