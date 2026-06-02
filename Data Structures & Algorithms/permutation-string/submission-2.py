class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #we're basically looking for a window of size len(s1) inside s2 that contains the same characters
        #so we could use a frequency map so figure that out.
        #that would be O(n * 26) time complexity since we check the freq maps each iteration
        #basically the same as the last sliding window problem.
        #In this problem we have on freq map for s1 and a dynamically changing freq map for our sliding window
        #in s2.

        s1_freq = [0] * 26
        s2_freq = [0] * 26
        
        #setting our freq map for s1
        for c in s1:
            s1_freq[ord(c) - ord('a')]+= 1


        l, r = 0, len(s1) - 1 #the window

        #populating the freq map for the window im starting with except the right pointer. i'll do that in the while loop
        for i in range(r):
            s2_freq[ord(s2[i]) - ord('a')] += 1
        

        while r < len(s2):
            s2_freq[ord(s2[r]) - ord('a')] += 1
            
            #if all indexes of the freq map match, then we found a permuation so return True
            all_same = True
            for i in range(26):
                if s1_freq[i] != s2_freq[i]:
                    all_same = False
            if all_same:
                return True

            #removing the left from the freq map for the window as we move forward
            s2_freq[ord(s2[l]) - ord('a')] -= 1

            #sliding window  
            l += 1
            r += 1
        
        #if we got out, then no permutations
        return False

        #O(n * 26) ~ O(n) time complexity and O(n) space b/c of our 2 freq maps.

