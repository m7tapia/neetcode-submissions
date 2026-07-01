class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #sort the arrays to have it like a number line with their positions
        #figure out at what time t each car will reach target doing (dest - pos) / speed
        #start at right b/c if a car from the left reaches the right, then they become a fleet
        #also keep track of the time of the last fleet

        #pair together so they stay with pair when sorting positions
        pairs = [(position[i], speed[i]) for i in range(len(position))]
        pairs.sort() #sorts least to greatest
        #list comprehension to get how long it takes each car to get to target
        times = [(target - pairs[i][0]) / pairs[i][1] for i in range(len(position))]

        time_of_last_fleet = 0
        count = 0
        for i in range(len(times) - 1, -1, -1):
            if times[i] > time_of_last_fleet:
                count +=1
                time_of_last_fleet = times[i]

        return count

        #O(nlog n) time and O(n) space






        
