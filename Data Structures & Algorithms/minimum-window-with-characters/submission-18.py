class Solution:
    def minWindow(self, s: str, t: str) -> str:

        def is_valid():
            for c in substr_freq:
                if window_freq.get(c, 0) < substr_freq[c]:
                    return False
            return True
    
        if not t or not s:
            return ''

        #this way is without the matched variable where we do a lot of repeating
        #checks and check every key in the map for every iteration and stop shrinking
        #when we find that one key is no longer greater than or equal to its equivalent in
        #the substr_freq map. This way is O(n * k) time complexity where k is the number of 
        #unique characters in our substring freq map. In this problem its bounded by the 
        #character set (52 for upper and lowercase letters) so really O(52n), so really
        #still O(n) but slightly less optimal.
        
        substr_freq = {}
        window_freq = {}
        
        for c in t:
            substr_freq[c] = substr_freq.get(c, 0) + 1
        
        l = 0
        min_length = float('inf')
        res = ''
        
        for r, c in enumerate(s):
            if c in substr_freq:
                window_freq[c] = window_freq.get(c, 0) + 1
            
            while is_valid():
                if r - l + 1 < min_length:
                    min_length = r - l + 1
                    res = s[l:r+1]
                if s[l] in substr_freq:
                    window_freq[s[l]] -= 1
                l += 1
        
        return res




