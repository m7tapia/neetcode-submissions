class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #we're basically looking for a window of size len(s1) inside s2 that contains the same characters
        #so we could use a frequency map so figure that out.
        #that would be O(n * 26) time complexity since we check the freq map each iteration
        #basically the same as the last sliding window problem

        s1_freq = [0] * 26
        s2_freq = [0] * 26

        for c in s1:
            s1_freq[ord(c) - ord('a')]+= 1


        l, r = 0, len(s1) - 1 #the window

        #populating the freq map for the window im starting with
        for i in range(r):
            s2_freq[ord(s2[i]) - ord('a')] += 1
        

        while r < len(s2):
            s2_freq[ord(s2[r]) - ord('a')] += 1
            
            all_same = True
            for i in range(26):
                if s1_freq[i] != s2_freq[i]:
                    all_same = False
            if all_same:
                return True

            #removing the left from the freq map for the window as we move forward
            s2_freq[ord(s2[l]) - ord('a')] -= 1
            
            
            l += 1
            r += 1
        
        return False

