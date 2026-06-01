class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        longest = 0
        hash_set = set()

        curr_length = 0
        
        while r < len(s):
            if s[r] not in hash_set:
                hash_set.add(s[r])
                r += 1
            else:
                hash_set.remove(s[l])
                l += 1

            curr_length = len(hash_set)
            longest = max(longest, curr_length)

        return longest



