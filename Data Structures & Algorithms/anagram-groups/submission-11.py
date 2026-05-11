class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}

        #use enumerate and unpacking to get iterate through each string and have easy access
        #to both the indices and strings
        for i, string in enumerate(strs):
            #list of size 26 of 0s
            li = [0] * 26

            #create the frequency key array
            for char in string:
                li[ord(char) - ord("a")]+= 1
            
            #turn the array into a string using join and a generator expression
            key = "#".join(str(val) for val in li)
            #use # delimiter to avoid some different strs appearing the same

            #if the key not already in the hash map create an empty list as the value
            if key not in map:
                map[key] = []
            # add the string to the key
            map[key].append(string)


        #create the list to return
        list = []
        for value in map.values():
            list.append(value)
        
        return list



