class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ''

        substr_freq = {}
        window_freq = {}
        
        #fill our substr freq map
        for c in t:
            substr_freq[c] = substr_freq.get(c, 0) + 1
        
        l = 0
        matched = 0
        min_length = float('inf')
        res = ''
        
        #its simpler to use a for r instead of while r. so we incr r each iteration and only when
        #our window is valid we shrink as much as we can by incr l
        for r, c in enumerate(s):
            #skip if not a character we care about
            if c in substr_freq:
                #add to our window freq map
                window_freq[c] = window_freq.get(c, 0) + 1
                #this is much better than doing the whole r_was_matched flag
                #when they equal thats when we add to matched, anything after that doesn't add to match
                if window_freq[c] == substr_freq[c]:
                    matched += 1
            #when we found a valid window, now we start shrinking it
            while matched == len(substr_freq):
                #r - l + 1 gives us the length
                #we record before we move l again
                if r - l + 1 < min_length:
                    min_length = r - l + 1
                    res = s[l:r+1]
                #skip over characters we don't care about
                if s[l] in substr_freq:
                    #remove char at l from freq map
                    window_freq[s[l]] -= 1
                    #if we don't have enough l characters in our string now, we no longer have a valid window
                    #so we're gonna break out of the while loop next iteration and our last recorded res is the
                    #shortest window in this valid result in our string
                    if window_freq[s[l]] < substr_freq[s[l]]:
                        matched -= 1
                #shrink
                l += 1
        
        return res