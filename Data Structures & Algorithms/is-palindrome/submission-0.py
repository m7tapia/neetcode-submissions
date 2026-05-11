class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = "".join(char.lower() for char in s if char.isalnum())

        front = 0
        end = len(string) - 1

        while front <= end:
            if string[front] != string[end]:
                return False
            front+= 1
            end -= 1
        
        return True