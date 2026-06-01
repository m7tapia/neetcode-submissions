class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        longest = 0
        hash_set = set()

        curr_length = 0
        
        while r < len(s):
            #if right pointer isnt in our set, add it and move right forward
            if s[r] not in hash_set:
                hash_set.add(s[r])
                r += 1
                #only have to keep track of length here b/c in the else, our window length is always decreasing
                #and we only care about the max length window
                curr_length = len(hash_set)
                longest = max(longest, curr_length)
            #if it is don't add right pointer and keep moving left forward until we get rid of our dupe
            else:
                hash_set.remove(s[l])
                l += 1

        return longest

        #O(n) time and O(n) space


        #The approach is the sliding window / 2 pointer. Keep a window of unique letters (using a set),
        #if we add a duplicate keep on removing from left until we get rid of the first one.

        #This way is using the in operator using a set.



