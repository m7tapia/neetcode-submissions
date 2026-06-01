class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #each k character can be a different character

        #sliding window, use a frequency array map for the letters of the alphabet
        #a window is valid if the characters inside it that aren't the most frequent
        #character is <= k b/c if that's true that means we can change those to get a window
        #of all the same characters. 
        #Whenever we get to a window that's no longer valid, we have to shrink our window until it is
        #again.

        l, r = 0, 1
        longest = 0

        while r <= len(s):
            freqs = [0] * 26
            substring = s[l:r]
            for c in substring:
                freqs[ord(c) - ord("A")] += 1

            most_freq = 0
            for freq in freqs:
                if freq > most_freq:
                    most_freq = freq

            num_other_chars = len(substring) - most_freq

            if k >= num_other_chars:
                longest = max(len(substring), longest)
                r += 1

            else:
                l += 1

        return longest
            
            