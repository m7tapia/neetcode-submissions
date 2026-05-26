class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()

        for i in range(len(nums) - 2):
            num = nums[i]
            l = i + 1
            r = len(nums) - 1
            while l < r:

                sum = num + nums[l] + nums[r]
                triplet = (num, nums[l], nums[r])

                if sum == 0:
                    if triplet not in res:
                        res.add(triplet)
                    l += 1
                    r -= 1
    

                if sum > 0:
                    r -= 1

                if sum < 0:
                    l += 1

        return [list(i) for i in res]


            


