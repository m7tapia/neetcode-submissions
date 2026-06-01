class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        longest = 0
        hash_set = set()
        curr_length = 0
        
        while r < len(s):
            prev_size = len(hash_set)
            hash_set.add(s[r])
            
            if prev_size == len(hash_set):
                # The character s[r] is a duplicate. 
                # Shrink the window from the left by removing s[l].
                hash_set.remove(s[l])
                l += 1
                # Do NOT remove s[r] here, and do NOT increment r.
                # On the next iteration, the loop will try to add s[r] again.
                # It will repeat this until the old instance of s[r] is cleared out.
            else:
                # s[r] was unique and successfully added to the set
                r += 1
                curr_length = len(hash_set)
                longest = max(longest, curr_length)
                
        return longest