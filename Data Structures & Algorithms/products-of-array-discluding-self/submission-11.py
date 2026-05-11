class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        pre_prod = 1
        for i in range(len(nums)):
            if i == 0:
                res[i] *= pre_prod
                continue
            pre_prod *= nums[i-1]
            res[i] *= pre_prod

        suf_prod = 1
        for i in range(len(nums) -1, -1, -1):
            if i == len(nums) -1:
                res[i] *= suf_prod
                continue
            suf_prod *= nums[i + 1]
            res[i] *= suf_prod

        return res