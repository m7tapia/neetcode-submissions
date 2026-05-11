class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return "None"
        return ("#:/".join(strs))
    def decode(self, s: str) -> List[str]:
        return s.split("#:/") if s != "None" else []