class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        longest = 0
        hash_set = set()
        curr_length = 0
        
        while r < len(s):
            prev_size = len(hash_set)
            hash_set.add(s[r])
            #see if a dupe was added
            if prev_size == len(hash_set):
                hash_set.remove(s[l])
                l += 1
                #if a dupe (s[r]) was found, the loop will keep on removing the left pointer until it finds where
                #the other s[r] and then remove both. Then we add s[r] again starting at this new unique substring.
                
            else: #if a dupe wasn't found keep on moving right pointer forward
                r += 1
                #we only have to keep track of our size here b/c in we're in the if statement the size of our window
                #is always decreasing and we want the max window
                curr_length = len(hash_set)
                longest = max(longest, curr_length)
                
        return longest