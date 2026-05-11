class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        #plus 1 b/c the 0 index isn't used, we need to have an index for 
        #if every number is the same in the list
        #index 1 stores # appears 1 time... index n stores # appears n times
        # our freq array is now of length 7: 0,1,2,3,4,5,6
        freq = [[] for i in range(len(nums) + 1)]

        #in map, numbers are keys, counts are values
        for i in nums:
            count[i] = 1 + count.get(i, 0) #the second arg is a default if get returns None
            #this would also work = (1 + count.get(i)) if count.get(i) else 1
        
        #now each bucket in the array represents a frequency and a list of numbers
        #that appear that number of times
        for num, ct in count.items():
            freq[ct].append(num)

        
        res = []
        #minus 1 here now b/c we want to start at index 6 not 7
        for i in range(len(freq) - 1, 0 , -1):
            #the nested loop only runs for the number of elements in the 
            #buckets
            for n in freq[i]:
                res.append(n)
                if (len(res)) == k:
                    return res

        #did it myself in solution 2


        


            


        
