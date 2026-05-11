class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre_prod, suf_prod, res = [1] * len(nums), [1] * len(nums), [0] * len(nums)
        
        #fill the prefix product array. the array that gets the sum of all going towards the right
        for i in range(0, len(nums)):
            if i == 0:
                pre_prod[i] = nums[i]
            else:
                pre_prod[i] = pre_prod[i-1] * nums[i]

        #fill the suffix product array. the array that gets the sum of all going towards the left
        for i in range(len(nums) - 1, 0, -1):
            if i == len(nums) - 1:
                suf_prod[i] = nums[i]
            else:
                suf_prod[i] = suf_prod[i+1] * nums[i]

        
        for i in range(len(nums)):
            #if i == 0, the index in the res array is going to be suf_prod[1] leading up to it
            if i == 0:
                res[i] = suf_prod[1]
            #if i is the last index, the index in the res array is going to be pre_prod[second last index] leading up to it
            elif i == len(nums) -1:
                res[i] = pre_prod[i - 1]
            #otherwise, it'll be the prefix sum to its left * the suffix sum to its right, excluding itself
            else:
                res[i] = pre_prod[i - 1] * suf_prod[i + 1]

        return res

        
        