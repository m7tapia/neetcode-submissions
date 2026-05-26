class Solution:
    def isPalindrome(self, s: str) -> bool:
        #use a 2 pointer approach

        l, r = 0, len(s) - 1

        #keep on going until pointers meet in the middle
        while l <= r:
            #skip if characters aren't alnphanumerical characters
            if not s[l].isalnum():
                l += 1
                continue

            if not s[r].isalnum():
                r -= 1
                continue
            
            #make sure its not case sensitive by using lowercase characters
            if s[l].lower() != s[r].lower():
                return False
            #increment pointers
            l += 1
            r -= 1

        return True


        #O(n) time complexity and O(1) space complexity since this is in place
        
