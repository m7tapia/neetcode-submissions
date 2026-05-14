class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #hashmap: key: string of the freq of each letter, value: list of strings that have that frequency of letters

        map = {}

        for s in strs:
            freq = [0] * 26

            for char in s:
                freq[ord(char) - ord("a")]+= 1

            key = "#".join(str(val) for val in freq)

            if key not in map:
                map[key] = []
            map.get(key).append(s)

        return [i for i in map.values()]

        #came back to it after a few days
        



            
