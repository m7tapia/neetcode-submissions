class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #each k character can be a different character

        #sliding window, use a frequency array map for the letters of the alphabet
        #a window is valid if the characters inside it that aren't the most frequent
        #in the string are <= k b/c if that's true that means we can change those to get a window
        #of all the same characters. 
        #Whenever we get to a window that's no longer valid, we slide our window. No need to shrink it
        #b/c why would we shrink our window after we've found a bigger valid window. We only care about
        #windows that are possibly bigger. If we made it smaller and didn't move r also, we would have to 
        #handle that when we make the window smaller, we increment s[r] in the freq map again at the top of the while loop

        l, r = 0, 0
        longest = 0
        freqs = [0] * 26

        while r < len(s): 
            #populate the freq as we go
            freqs[ord(s[r]) - ord("A")] += 1

            #find how many times the most frequent character comes up
            most_freq = 0
            for freq in freqs:
                if freq > most_freq:
                    most_freq = freq

            substring = s[l:r + 1]
            #find how many characters there are that aren't the most frequent character
            num_other_chars = len(substring) - most_freq

            #check we have enough k switches to make this window valid
            if k >= num_other_chars:
                #keep track of our longest valid window
                longest = max(len(substring), longest)
                #make window bigger
                r += 1 
            
            #if we don't have enough k switches to make window valid, slide window to the right.
            #No need to make it smaller b/c we only care about what could be bigger.
            else:
                freqs[ord(s[l]) - ord("A")] -= 1
                l += 1
                r += 1

        return longest


        #This is O(n * 26) ~ O(n) time complexity and O(26) ~ O(1) space complexity
            
            