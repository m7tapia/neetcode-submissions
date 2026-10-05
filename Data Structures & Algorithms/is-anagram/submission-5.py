class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #create a list of size 26 with default value 0
        arr = [0] * 26

        #iterate through s
        for i in range(len(s)):
            #use ord() to get ascii
            arr[ord(s[i]) - ord("a")] += 1
        
        #iterate through t
        for i in range(len(t)):
            arr[ord(t[i]) - ord("a")] -= 1

        for i in arr:
            if i != 0: 
                return False
            
        return True

