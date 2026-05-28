class Solution:
    def trap(self, height: List[int]) -> int:
        #keep track of the max heights on each side
        maxL, maxR, = height[0], height[-1], 
        #we can skip the ends b/c we know that they can't hold any water since its not a container
        l, r = 1, len(height) - 2
        #we use two pointers
        total_trapped = 0
        
        #we need to make sure that we only move the pointer that has the lowest max. we don't need to know
        #the other side, we just need to know that each time we move the pointer, we're moving the lower max.
        #before moving each pointer, since we know the max height the water can fill at that index, we can 
        #calculate the water filled there.
        while l <= r:
            if maxL < maxR:
                trapped = maxL - height[l]
                total_trapped += trapped if trapped > 0 else 0
                maxL = max(maxL, height[l])
                l += 1

            else:
                trapped = maxR - height[r]
                total_trapped += trapped if trapped > 0 else 0
                maxR = max(maxR, height[r])
                r -= 1

        return total_trapped

        #This 2 pointer approach is O(n) time and O(1) space

            




