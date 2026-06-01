class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #each k character can be a different character

        #sliding window, use a frequency array map for the letters of the alphabet
        #a window is valid if the characters inside it that aren't the most frequent
        #character is <= k b/c if that's true that means we can change those to get a window
        #of all the same characters. 
        #Whenever we get to a window that's no longer valid, we have to shrink our window until it is
        #again.

        l, r = 0, 0
        longest = 0
        freqs = [0] * 26

        while r < len(s): 
            freqs[ord(s[r]) - ord("A")] += 1

            most_freq = 0
            for freq in freqs:
                if freq > most_freq:
                    most_freq = freq

            substring = s[l:r + 1]
            num_other_chars = len(substring) - most_freq

            if k >= num_other_chars:
                longest = max(len(substring), longest)
                r += 1

            else:
                freqs[ord(s[l]) - ord("A")] -= 1
                l += 1
                r += 1

        return longest
            
            