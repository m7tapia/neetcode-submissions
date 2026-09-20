class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # an array size 26 to figure out anagram
        # hashmap key is that 26 string for each anagram

        map = {}

        for s in strs:
            seq = [0] * 26
            for c in s:
                seq[ord(c) - ord('a')] += 1

            key = '#'.join(str(val) for val in seq)

            if key not in map:
                map[key] = []
            map[key].append(s)

        return [val for val in map.values()] 