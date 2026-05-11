class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #we have to do our prefix product then do our suffix product in the res array
        #and on each we ignore the index we're currently on and just focus on what has passed
        res = [1] * len(nums)

        pre_prod = 1
        #do the prefix product. On the res array, we ignore the corresponding index in the nums array
        #since we want to exclude that one
        for i in range(len(nums)):
            #if i == 0, there's nothing to prefix product so the prefix product is 1 so res[i] is 1 here
            if i == 0:
                res[i] *= pre_prod
                continue
            #multiply res[i] by the prefix product leading up to it but excluding itself
            pre_prod *= nums[i -1]
            res[i] *= pre_prod

        suf_prod = 1               #[inclusive, exclusive]
        for i in range(len(nums) -1, -1, -1):
            #if i is the last index, there's no suffix product after it
            if i == len(nums) -1:
                res[i] *= suf_prod
                continue
            #multiply res[i] by the suffix product leading up to it but excluding itself
            suf_prod *= nums[i + 1]
            res[i] *= suf_prod

        return res
            
        

