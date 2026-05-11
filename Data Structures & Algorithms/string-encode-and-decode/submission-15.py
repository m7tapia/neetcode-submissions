class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs: 
            return "None"
        return "#/*".join(strs)
    def decode(self, s: str) -> List[str]:
        if s == "None":
            return []
        return s.split("#/*")


        #A problem I had is If the list was just an empty list and I used the join, it would become just an empty string. 
        #If the list was a list with just an empty string in there, then it would also become an empty string. 
        #In the decode, I would have no way to distinguish them, so that's why I have the `None`, 
        #which distinguishes them in the decoder. 

        #The solution is not the best because if the string happens to have #/*, then it would mess up the decoder. 