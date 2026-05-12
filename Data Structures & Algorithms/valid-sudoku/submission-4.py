class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #for rows do a set in each iteration
        #for columns: index: y-value, contains: set of numbers in that column
        #if we're trying to add a duplicate to the set then it's invalid

        #for the 3x3 groups we're using a hashmap and for each coordinate we're on we find a group
        # (x // 3, y //3) and that gives us a group. we put that group in a hashmap and the value
        #is a set. If we try to add a new number to that set, we return false.

        #we create a columns array for each column and use a set in each and a map for the groups
        columns, groups = [set() for _ in range(9)], {}
        
        for y, i in enumerate(board):
            
            x_map = set()
            #first for each row we use a set
            for index, s in enumerate(i):
                if s == ".":
                    continue
                if s in x_map:
                    return False
                x_map.add(s)

                #for each column we check the set, if not in there we add it.
                if s in columns[index]:
                    return False
                columns[index].add(s)

                #now for the 3x3 groups
                #find the group
                #(say 5 //3, 8 //3) = (1, 2) is our group. (second row, third column)
                group = (index // 3, y // 3)
                if group not in groups:
                    groups[group] = set() 
                if s in groups[group]:
                    return False
                groups[group].add(s)

        return True

        #time complexity is O(r x c) but really O(9 x 9) here since it's a sudoku board
        #so constant time.

        #space complexity is also O(1) because our input size will never grow


        #did this mostly myself with some hints. hint mostly for the group (doing the // 3 to get the groups) 
                
