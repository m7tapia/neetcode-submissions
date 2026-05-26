class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        front, end = 0, len(numbers) - 1

        while True:
            sum = numbers[front] + numbers[end]

            if sum == target:
                return [front + 1, end + 1]

            if sum > target:
                end -= 1

            else:
                front += 1

            