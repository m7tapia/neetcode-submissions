class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = []
        for i in range(len(nums)):
            prod = 1
            for j in range(len(nums)):
                if j == i:
                    continue
                prod *= nums[j]
            arr.append(prod)
        
        return arr

        #this was my first try no help, had to do it the brute force way
        #O(n^2) time complexity




                
                