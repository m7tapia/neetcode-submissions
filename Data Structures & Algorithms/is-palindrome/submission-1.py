class Solution:
    def isPalindrome(self, s: str) -> bool:

        #use a generator expression to create a new string that's all lower-case and only valid
        #alphanumeric characters
        string = "".join(char.lower() for char in s if char.isalnum())

        #2 pointers
        front = 0
        end = len(string) - 1

        #incr front and decrement end; if they're ever not equal then its not a palindrome
        while front <= end:
            if string[front] != string[end]:
                return False
            front+= 1
            end -= 1
        
        return True