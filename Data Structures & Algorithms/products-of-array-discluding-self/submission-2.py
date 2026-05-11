class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #first get the product of them all
        prod, arr, zero_count = 1, [0 for i in nums], 0

        #find the # of zeros in nums
        for num in nums:
            if num == 0:
                zero_count += 1
        #if there's more than one zero in the array, the whole array will be 0's
        if zero_count > 1:
            return arr
        
        #if there's no zeros in the array, don't have to worry about zeros
        if zero_count == 0:
            for num in nums:
                prod *= num
            for i in range(len(nums)):
                arr[i] = prod // nums[i]
            return arr

        #if there's one zero in the array
        
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

