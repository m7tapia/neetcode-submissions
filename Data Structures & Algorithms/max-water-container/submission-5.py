class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r, max_area = 0, len(heights) - 1, 0

        while l < r:
            l_height, r_height = heights[l], heights[r]
            area = min(l_height, r_height) * (r - l)
            max_area = max(max_area, area)

            if l_height < r_height:
                l += 1
            else:
                r -= 1

        return max_area

