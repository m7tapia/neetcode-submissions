class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        front, end = 0, len(numbers) - 1

        #can use a while True loop b/c a solution is guaranteed in this problem
        while True:
            sum = numbers[front] + numbers[end]

            if sum == target:
                return [front + 1, end + 1]

            if sum > target:
                end -= 1

            else:
                front += 1

            #two pointers. We use the fact that the list is sorted. 
            #if our sum > target we move left pointer forward
            #if our sum < target we move right pointer back
            
            #O(n) time complexity and O(1) space complexity