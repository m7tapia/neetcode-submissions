class Solution:

    def encode(self, strs: List[str]) -> str:
        
        if len(strs) == 0:
            return "None"
        return ("#:/".join(strs))
    def decode(self, s: str) -> List[str]:
        return s.split("#:/") if s != "None" else []

        #the difficult part was differentiating an empty list from a list that just had empty quotes, 
        #because they are both false-y. To fix that, if the list was actually empty, 
        #I would just return None in the encode function and handle that in the decode function. 

        #I did this solution myself, which is not the best because if the delimiter "#:/" is
        #somehow in the list, it'll mess up the result.