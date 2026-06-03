class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ''
        
        substr_freq = {}
        window_freq = {}
        
        for c in t:
            substr_freq[c] = substr_freq.get(c, 0) + 1
        
        l = 0
        min_length = float('inf')
        res = ''
        
        def is_valid():
            for c in substr_freq:
                if window_freq.get(c, 0) < substr_freq[c]:
                    return False
            return True
        
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


