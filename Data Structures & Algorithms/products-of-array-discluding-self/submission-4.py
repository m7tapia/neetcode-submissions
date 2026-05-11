class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, arr, zero_count = 1, [0 for i in nums], 0

        #find the # of zeros in nums
        for num in nums:
            if num == 0:
                zero_count += 1
        #case 1: if there's more than one zero in the array, the whole array will be 0's
        if zero_count > 1:
            return arr
        
        #case 2: if there's no zeros in the array, don't have to worry about zeros
        if zero_count == 0:
            for num in nums:
                prod *= num
            for i in range(len(nums)):
                arr[i] = prod // nums[i]
            return arr

        #case 3: if there's one zero in the array, the index that had the zero will be the product of all the rest
        #and all the rest will be 0s
        
        #first find where the zero is
        zero_index = 0
        for index, num in enumerate(nums):    
            if num == 0:
                zero_index = index
        
        #now find the product without the zero
        for i, num in enumerate(nums):
            if i != zero_index:
                prod *= num
        
        for i, num in enumerate(arr):
            if i != zero_index:
                arr[i] = 0
            else:
                arr[i] = prod
        return arr


        #this is O(n) time and O(n) space complexity
        #also did it the bad way b/c I used the divison operator

