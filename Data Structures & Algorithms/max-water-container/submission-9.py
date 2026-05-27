class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r, max_area = 0, len(heights) - 1, 0

        while l < r:
            l_height, r_height = heights[l], heights[r]
            #calculate the area by lowest height * width
            area = min(l_height, r_height) * (r - l)
            #update max_area if we found a bigger area
            max_area = max(max_area, area)

            #we want to keep moving inward to see if we get a bigger area, so we want to obviously keep the taller bar and move the shorter one
            if l_height < r_height:
                l += 1
            else: #if both bars are same height, we can move either, it doesn't matter b/c our max_height is still bottlenecked by our lowest bar, so there's no way we could get higher than what we just got.
                r -= 1

        return max_area



#this uses a 2 pointer approach. we start at the ends. we keep track of our max_area found. we keep moving inward
#to see if we find a greater area. #we move the shorter bar inward b/c that gives us the most potential for max area.
#we stop once l and r meet in the middle and return the max area we found.

#O(n) time complexity and O(1) space complexity
