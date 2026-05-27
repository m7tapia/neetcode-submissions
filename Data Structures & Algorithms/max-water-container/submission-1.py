class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0

        for i in range(len(heights)):
            i_height = heights[i]
            for j in range(i + 1, len(heights)):
                j_height = heights[j]
                min_height = j_height if j_height < i_height else i_height
                area = min_height * (j - i)
                if area > max_area:
                    max_area = area

        return max_area
