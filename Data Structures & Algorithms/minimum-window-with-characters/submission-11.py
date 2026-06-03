class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #we use 2 freq maps. One for t and one for our window. We only care about the letters
        #that are in t. We keep on increasing our window until we find a window that contains
        #atleast all the letters in t. Then keep decreasing until our window is no longer valid.
        #That is one possible result. We keep on doing this until we get to the end and find the shortest
        #result. Instead of having to compare our maps for each letter each time we keep track of
        #how many letters show up enough times using a matched variable.

        substr_freq = {}
        window_freq = {}
        l, r = 0, 0
        matched = 0
        min_length = float('inf')
        res = ''

        #fill substr freq map
        for c in t:
            substr_freq[c] = substr_freq.get(c, 0) + 1
        
        while r < len(s):
            #if we don't have all chars we need yet we are making window bigger
            if matched < len(substr_freq):
                #skip chars we dont care abt
                if s[r] not in substr_freq:
                    r += 1
                    continue
        #s[r] may not have been in window freq yet
                if s[r] in window_freq and window_freq[s[r]] >= substr_freq[s[r]]:
                    #we need to know if the char at r already had enough, if they didnt and now they do we incr matched
                    r_was_matched = True
                else: 
                    r_was_matched = False
                window_freq[s[r]] = window_freq.get(s[r], 0) + 1
                if not r_was_matched and window_freq[s[r]] >= substr_freq[s[r]]:
                    matched += 1

                r += 1
            

            else: #if matched == len(substr_freq)
            #we need this loop in order to shrink our window to get the smallest window
                while matched == len(substr_freq):
                    if s[l] in substr_freq:
                        window_freq[s[l]] = window_freq.get(s[l], 0) - 1

                        if window_freq[s[l]] < substr_freq[s[l]]:
                            matched -=1
                    l += 1
                #now that we have the smallest we can get this valid window, check if its the smallest valid window we've found
                #in the string and record it if it is
                if min_length > r - l:
                    min_length = r - l
                    res = s[l - 1: r]

            #I have to do this shrink loop again here, just in case the edge case where a valid
            #window goes all the way to the end of the string and my else block never runs for that 
            #window which handles making it the result if its the min. This will
            #catch that. I just copied my else block.
            
            while matched == len(substr_freq):
                if s[l] in substr_freq:
                    window_freq[s[l]] = window_freq.get(s[l], 0) - 1

                    if window_freq[s[l]] < substr_freq[s[l]]:
                        matched -=1
                l += 1

                if min_length > r - l:
                    min_length = r - l
                    res = s[l - 1: r]

                    
        return res


        #O(n) time complexity and O(1) space complexity
        #But i did this mostly myself with some help debugging
                


        

        




            
                        


