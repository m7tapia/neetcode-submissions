class Solution:
    def trap(self, height: List[int]) -> int:
        maxL, maxR, = height[0], height[-1], 
        #we can skip the ends b/c we know that they can't hold any water since its not a container
        l, r = 1, len(height) - 2

        total_trapped = 0
        while l <= r:
            if maxL < maxR:
                trapped = min(maxL, maxR) - height[l]
                total_trapped += trapped if trapped > 0 else 0
                maxL = max(maxL, height[l])
                l += 1

            else:
                trapped = min(maxR, maxL) - height[r]
                total_trapped += trapped if trapped > 0 else 0
                maxR = max(maxR, height[r])
                r -= 1

        return total_trapped

            




