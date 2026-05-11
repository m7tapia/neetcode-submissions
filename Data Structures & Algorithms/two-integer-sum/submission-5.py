class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        #enumerate and unpack to have both index and value in each iteration
        for i, num in enumerate(nums):

            #calculate complement
            complement = target - nums[i]

            #check if complement is already in the map
            if complement in map:
                return [map[complement], i]

            #if not add current iteration to map to remember it
            map[num] = i

        #this will never run since there will always be a combination that sums to complement
        return []