class Solution:


    #In this solution, We want to know the length of our string, but we 
    #can't store it in an array and pass it to the decoder because our functions can't be stateful. 
    #They have to be stateless, so we have to hide the length in our string. We can do that by having a 
    #number that represents the length, and then having a pound, which is our delimiter. Then, whenever we get there, 
    #we know the next five or whatever characters are that substring. 
    def encode(self, strs: List[str]) -> str:
        arr = []
        for i in strs:
            arr.append(str(len(i)))
            arr.append("#")
            arr.append(i)
            #same thing
            #arr = [f"{str(len(string))}#{string}" for string in strs]

        return "".join(arr)
        

    def decode(self, s: str) -> List[str]:
        res, i = [], 0

        #pointer to start of substring
        while i < len(s):
            j = i
            #find where pound is
            while s[j] != "#":
                j += 1
            #number is between i and j [inclusive, exclusive]
            length = int(s[i : j])

            #append the substring now to the list
            res.append(s[j+1: j+1 + length])

            #move i to the next part
            i = j + 1 + length

        return res


    #This solution handles what I was handling with None in my previous solution. 
    #If it's an empty string in the list, then it still gets a delimiter, pound, and zero. 
    #If it's an actual empty list, it doesn't get anything. 

    #This is fool proof b/c even if the list has a number than a pound somewhere, we will never treat those as delimiters because
    #we'll get to to the delimiter we put first, and their pound will just be in the substring.
    
    #This is O(n) time and space


 
        

        