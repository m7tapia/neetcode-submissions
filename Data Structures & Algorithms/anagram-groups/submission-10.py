class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}

        for i, string in enumerate(strs):
            li = [0] * 26

            for char in string:
                li[ord(char) - ord("a")]+= 1
            
            key = "#".join(str(val) for val in li)
            #use # delimiter to avoid some different strs appearing the same

            #if the key not already in the hash map create an empty list as the value
            if key not in map:
                map[key] = []
            # add the string to the key
            map[key].append(string)


        list = []

        for value in map.values():
            list.append(value)
        
        return list



