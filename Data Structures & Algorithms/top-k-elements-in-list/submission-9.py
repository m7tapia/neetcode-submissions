import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #this is a less optimal way using heaps
        map = {}
        for i in nums:
            map[i] = 1 + map.get(i,0)

        heap = []
        #a min heap compares a tuple in order front to back
        for (num, freq) in map.items():
            heapq.heappush(heap, (freq, num))

            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        while heap:
            res.append(heapq.heappop(heap)[1])

        return res

