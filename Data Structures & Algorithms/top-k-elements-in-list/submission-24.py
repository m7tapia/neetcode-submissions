class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {i: [] for i in range(len(nums) + 1)} #keys are going to be the frequency, #map will be size len(nums)
        #values will be a list of the numbers that appear that frequency
        #need to +1 b/c we would never get 0 freq but we would get the len(nums) freq if every number is the same
        freq = {}
        for i in nums:
            if i not in freq:
                freq[i] = 0
            freq[i] +=1

        for num, freq in freq.items():
            map[freq].append(num)

        #now we have buckets of numbers that all have same frequency going upwards
        #now all we have to do is iterate backwards
        
        res = []
        for bucket in range(len(map) -1, -1, -1):
            for num in map[bucket]:
                res.append(num)
                if len(res) == k:
                    return res
        return []

        

        



