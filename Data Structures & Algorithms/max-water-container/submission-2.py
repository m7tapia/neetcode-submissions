class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0

        for i in range(len(heights)):
            i_height = heights[i]
            #starting one ahead of i b/c if we start from the beginning for j, we will be redoing combinations we've already done
            for j in range(i + 1, len(heights)):
                j_height = heights[j]
                min_height = j_height if j_height < i_height else i_height
                area = min_height * (j - i)
                if area > max_area:
                    max_area = area

        return max_area


        #this is the brute force solution. checking every single combination to see which one gives us
        #the most area
        #O(n^2) time complexity and O(1) space complexity


        #for this problem the area of each combination is the height of the shorter bar * the space between both bars.
