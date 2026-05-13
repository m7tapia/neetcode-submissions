class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #the optimal solution is to use convert the nums into a set
        #now the tricky part is finding the start of a sequence
        #if our number is 100 and is the start of the sequence, then it won't have a left neighbor 99 in the set.
        #That's how we identify the start of a sequence.

        uniq_nums = set(nums)
     
        highest_count = 1
        #go through each unique number
        for num in uniq_nums:
            count = 1
            #We only enter this if it's the start of a sequence!
            if num - 1 not in uniq_nums:
                next = num + 1
                #keep on checking if there's the next number in the set
                while next in uniq_nums:
                    count += 1
                    next += 1
            #if count is higher than our highest, than update highest
            if count > highest_count:
                highest_count = count
        #if nums is empty we want to return 0 not 1
        return highest_count if nums else 0


#this is O(n) time and O(n) space. O(n) time b/c we only iterate each number once.
#Remember unless the number is the start of a sequence we don't start the inner loop.

