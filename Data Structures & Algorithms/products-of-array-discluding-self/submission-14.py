class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        pre_prod = 1
        for i in range(len(nums)):
            if i != 0:
                pre_prod *= nums[i - 1]
            res[i] *= pre_prod
            
            
        post_prod = 1
        for i in range(len(nums) - 1, -1, -1):
            if i != len(res) -1:
                post_prod *= nums[i + 1]
            res[i] *= post_prod

        return res
