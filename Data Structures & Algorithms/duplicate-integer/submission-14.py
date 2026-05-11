class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        li = []
        for i in nums:
            if i in li:
                return True
            li.append(i)
        return False

        #here we just iterate through, first check if each is in List already
        #if it is return True, if it isn't add it to array. If we reach the end
        #return False. #set also would've worked but in this case there's no reason
        #to use a set over a list
            