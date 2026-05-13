class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #the optimal solution is to use convert the nums into a set
        #now the tricky part is finding the start of a sequence
        #if our number is 100 and is the start of the sequence, then it won't have a left neighbor 99 in the set.
        #That's how we identify the start of a sequence.

        if not nums:
            return 0

        uniq_nums = set(nums)



        highest_count = 1
        for num in uniq_nums:
            count = 1
            if num - 1 not in uniq_nums:
                next = num + 1
                while next in uniq_nums:
                    count += 1
                    next += 1
            if count > highest_count:
                highest_count = count
                
            
        return count if count > highest_count else highest_count


