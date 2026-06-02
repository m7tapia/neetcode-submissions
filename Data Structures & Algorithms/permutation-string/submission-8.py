class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #this is a slightly more efficient way to do it. still using our two freq maps but we 
        #don't have to iterate through them each iteration of our while loop. We keep track of
        #of how many matches we have in a variable.
        s1_freq = [0] * 26
        s2_freq = [0] * 26
        matches = 0
        
        #setting our freq map for s1
        for c in s1:
            s1_freq[ord(c) - ord('a')]+= 1

        l, r = 0, len(s1) - 1 #the window

        #populating the freq map for the window im starting with except right pointer.
        for i in range(r):
            s2_freq[ord(s2[i]) - ord('a')] += 1

        #getting all the matches in our window except for the one at r
        for i in range(26):
            if s1_freq[i] == s2_freq[i]:
                matches += 1

        while r < len(s2):
            #add r to our freq map for our window
            s2_freq[ord(s2[r]) - ord('a')] += 1 
            #setting variables just to make it easier and clearer
            s1_freq_at_r = s1_freq[ord(s2[r]) - ord('a')]
            s2_freq_at_r = s2_freq[ord(s2[r]) - ord('a')]
            

            #adjust matches for r
            #if we now have a match, that means we couldn't have had one before so incr matches
            if s2_freq_at_r == s1_freq_at_r:
                matches += 1
            #if we don't have a match now but we did before, decr matches
            elif s2_freq_at_r - 1 == s1_freq_at_r:
                matches -= 1
            #otherwise that means we didn't have a match before and we don't now so don't do anything to matches
            
            #check if our window is an anagram of s1
            if matches == 26:
                return True
            
            #window not anagram so start shifting window and removing l from matches

            #removing l from our window freq map
            s2_freq[ord(s2[l]) - ord('a')] -= 1
            #setting variables just to make it easier and clearer
            s1_freq_at_l = s1_freq[ord(s2[l]) - ord('a')]
            s2_freq_at_l = s2_freq[ord(s2[l]) - ord('a')]

            #adjusting matches
            if s2_freq_at_l == s1_freq_at_l:
                matches += 1
            elif s2_freq_at_l + 1 == s1_freq_at_l:
                matches -= 1
            
            #sliding window
            l += 1
            r += 1

        return False

        #O(n) time complexity and O(1) space complexity b/c our maps are fixed size
        

        