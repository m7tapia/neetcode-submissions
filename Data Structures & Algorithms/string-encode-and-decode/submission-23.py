class Solution:

    def encode(self, strs: List[str]) -> str:
        arr = []
        for s in strs:
            arr.append(f"{len(s)}#{s}")

        return "".join(arr)

    def decode(self, s: str) -> List[str]:
        res = []
        start, x = 0, 0

        while start < len(s):
            while s[x] != "#":
                x += 1
            length = int(s[start: x])
            res.append(s[x + 1: x + 1 + length])
            start,x  = x + 1 + length, x + 1 + length

        return res

