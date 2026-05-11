import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #this is a less optimal way using heaps
        map = {}
        for i in nums:
            map[i] = 1 + map.get(i,0)

        heap = []
        #a min heap compares a tuple in order front to back, compares index 0 then 1
        for (num, freq) in map.items():
            #we want the heap to order using the freq
            heapq.heappush(heap, (freq, num))

            #if the heap gets too long we pop the least frequencies since we want the top k frequencies
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        while heap:
            #now return an array of just the numbers of the top k frequencies
            res.append(heapq.heappop(heap)[1])

        return res


        #time complexity O(nlogn) b/c we push to the heap for every item in the hashmap and the 
        #hashmap is as long as every unique number in the List
        #space complexity is O(n + k) b/c we use a hashmap and the heap could be as long as k
