class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        y_set = [set() for i in range(9)]
        x_set = [set() for i in range(9)]
        groups = {}

        for i, row in enumerate(board):
            for j, num in enumerate(row):
                if num == ".":
                    continue
                if num in x_set[i]:
                    return False
                x_set[i].add(num)
                
                if num in y_set[j]:
                    return False
                y_set[j].add(num)
                
                group = (j // 3, i // 3)
                if group not in groups:
                    groups[group] = set()
                
                if num in groups.get(group):
                    return False
                groups[group].add(num)

        return True