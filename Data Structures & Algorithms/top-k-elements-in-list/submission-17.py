import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for i in nums:
            map[i] = 1 + map.get(i, 0)

        heap = []
        for num, freq in map.items():
            heapq.heappush(heap, (freq, num))

            if len(heap) > k:
                heapq.heappop(heap)
            
        res = []
        while heap:
            res.append(heapq.heappop(heap)[1])

        return res