class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # O(n)^2 nested loop going thru and 
        
        map = {}

        for i, num in enumerate(nums):

            complement = target - num

            if complement in map:
                return[map[complement], i]

            map[num] = i

