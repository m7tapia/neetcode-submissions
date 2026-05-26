class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()

        for i in range(len(nums) - 2):
            num = nums[i]
            l = i + 1
            r = len(nums) - 1
            while l < r: #not while l <= r b/c all numbers should be distinct

                sum = num + nums[l] + nums[r]
                triplet = (num, nums[l], nums[r])

                if sum == 0:
                    if triplet not in res:
                        res.add(triplet)
                    #in/decrement both since if sum is 0, changing only one will never give us 0
                    l += 1
                    r -= 1
    

                if sum > 0:
                    r -= 1

                if sum < 0:
                    l += 1

        return [list(i) for i in res] #list() turns the tuple to a list

        #so first we sorted the array in ascending order. #then we used two loops.
        #the first loop goes through each first number except the last two which is for our two pointers. 
        #the inner loop it's like a regular two sum problem. since our input arry is sorted now, 
        #we can use two pointer approach instead of the hashmap to save memory. 
        #when we find a triplet we check if that triplet
        #is already in our res set. #since nums is sorted, if there's a dupe the tuple
        #will have the numbers in the same order. #if there's a dupe don't add to res and move on.
        #if sum < 0 move left pointer. if sum < 0 move right pointer.
        #going through both loops will give us all non duplicate triplets.
        

        #time complexity is O(nlogn) + O(n^2) so O(n^2)

        #space complexity is O(k) where k is the # of unique triplets + memory used in sorting algorithm

            


