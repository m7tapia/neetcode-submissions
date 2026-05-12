class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #for rows do a set in each iteration
        #for columns: index: y-value, contains: set of numbers in that column
        #if we're trying to add a duplicate to the set then it's invalid

        columns = [set() for _ in range(9)]
        groups = {}

        for y, i in enumerate(board):
            x_map = set()
            for index, s in enumerate(i):
                if s == ".":
                    continue
                if s in x_map:
                    return False
                x_map.add(s)

                if s in columns[index]:
                    return False
                columns[index].add(s)

                #now for the 3x3 groups
                group = (index // 3, y // 3)
                if group not in groups:
                    groups[group] = set() 
                if s in groups[group]:
                    return False
                groups[group].add(s)

        return True
                
