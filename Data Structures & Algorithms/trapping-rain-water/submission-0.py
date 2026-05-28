class Solution:
    def trap(self, height: List[int]) -> int:
        max_left, max_right = [0] * len(height), [0] * len(height)

        highest = 0
        for i in range(len(height)):
            if i == 0:
                max_left[i] = 0
                continue
            highest = max(highest, height[i - 1])
            max_left[i] = highest

        highest = 0
        for i in range(len(height) -1, -1, -1):
            if i == len(height) - 1:
                max_right[i] = 0
                continue
            highest = max(highest, height[i + 1])
            max_right[i] = highest

        total_trapped = 0
        for i, h in enumerate(height):
            trapped_water_in_col = min(max_right[i], max_left[i]) - h
            total_trapped += trapped_water_in_col if trapped_water_in_col > 0 else 0

        return total_trapped

