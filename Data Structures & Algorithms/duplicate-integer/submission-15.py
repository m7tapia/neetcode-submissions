class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for i in nums:
            s.add(i)
        if len(s) != len(nums):
            return True
        return False

        #we just add all elements to a set, if the length of the set is
        #shorter than the list, than there was a duplicate so return True