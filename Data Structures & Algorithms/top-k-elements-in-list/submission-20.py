class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        buckets = [[] for i in range(len(nums) + 1)]

        for i in nums:
            #the map now has a key for each unique # and the value is how many times its in nums
            map[i] = map.get(i, 0) + 1

        for num, freq in map.items():
            buckets[freq].append(num)

        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for n in buckets[i]:
                res.append(n)
                if len(res) == k:
                    return res

        


        