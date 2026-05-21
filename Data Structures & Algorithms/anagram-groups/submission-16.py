class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}

        for s in strs:
            freq = [0] * 26
            for c in s:
                freq[ord(c) - ord("a")]+= 1

            key = "$".join(str(i) for i in freq)

            if key not in map:
                map[key] = []
            map[key].append(s)

        res = []
        for val in map.values():
            res.append(val)
        return res

