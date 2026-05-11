class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "None"
            #handles the difference between an empty list and a [""] b/c in a string "".
            #"" could mean empty list or [""] if i returned "".
        arr = []
        for i in strs:
            arr.append(str(len(i)))
            arr.append("#")
            arr.append(i)
            #same thing
            #arr = [f"{str(len(string))}#{string}" for string in strs]

        return "".join(arr)
        

        
        
    def decode(self, s: str) -> List[str]:
        if s == "None":
            return []

        res, i = [], 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i : j])

            res.append(s[j+1: j+1 + length])

            i = j + 1 + length

        return res

        

        