class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre_prod, post_prod, res = [1] * len(nums), [1] * len(nums), [0] * len(nums)
        
        #fill the pre product array. the array that gets the sum of all going towards the right
        for i in range(0, len(nums)):
            if i == 0:
                pre_prod[i] = nums[i]
            else:
                pre_prod[i] = pre_prod[i-1] * nums[i]

        #fill the post product array. the array that gets the sum of all going towards the left
        for i in range(len(nums) - 1, 0, -1):
            if i == len(nums) - 1:
                post_prod[i] = nums[i]
            else:
                post_prod[i] = post_prod[i+1] * nums[i]

        for i in range(len(nums)):
            if i == 0:
                res[i] = post_prod[1]
            elif i == len(nums) -1:
                res[i] = pre_prod[i - 1]
            else:
                res[i] = pre_prod[i - 1] * post_prod[i + 1]

        return res

        
        