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

        for i in range(len(arr)):
            if i == 0:
                continue
            if arr[i] == arr[i-1] + 1:
                count += 1

            else:
                if top_count < count:
                    top_count = count
                count = 1

        return top_count if top_count > count else count
            

        #this is the simplest approach. we sort the array, we also make sure to eliminate dupes
        #before hand bc we only need one of each number. if we had 1 1, 2, 3 that dupe would mess
        #up our count. And we count the longest sequence. This is not a good approach b/c it's
        #O(nlogn) time b/c we sort. Also O(n) space. We need to find a way to do it with better time
        #complexity.