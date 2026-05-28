class Solution:
    def trap(self, height: List[int]) -> int:
        #we have to look at each column seperately. make two arrays to see the highest bar to each side
        #then for each column the amount of water trapped is the lowest max height on either side - the height of our current bar. 
        #if negative make it 0 b/c we cant hold negative water.
        max_left, max_right = [0] * len(height), [0] * len(height)

        #getting the array to hold the highest bar to the left of each bar
        highest = 0
        for i in range(len(height)):
            if i == 0:
                max_left[i] = 0
                continue
            highest = max(highest, height[i - 1])
            max_left[i] = highest

        #getting the arry to hold the highest bar to the right of each bar
        highest = 0
        for i in range(len(height) -1, -1, -1):
            if i == len(height) - 1:
                max_right[i] = 0
                continue
            highest = max(highest, height[i + 1])
            max_right[i] = highest

        #now for every index, the amount of water trapped is the shorter max height on either side (since thats the bottleneck)
        # minus the height of the bar itself. if negative, means can't hold any so add 0 to total.
        total_trapped = 0
        for i, h in enumerate(height):
            trapped_water_in_col = min(max_right[i], max_left[i]) - h
            total_trapped += trapped_water_in_col if trapped_water_in_col > 0 else 0

        return total_trapped


        #this method is O(n) time and O(n) space complexity
