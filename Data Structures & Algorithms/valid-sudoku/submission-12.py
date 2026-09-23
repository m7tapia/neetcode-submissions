class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = [set() for _ in range(9)]
        rows = [set() for _ in range(9)]
        groups = {}
        
        for i, row in enumerate(board):
            for j, num in enumerate(row):
                if num == ".":
                    continue
                if num in cols[j]:
                    return False
                cols[j].add(num)

                if num in rows[i]:
                    return False
                rows[i].add(num)

                group = (j // 3, i // 3)
                if group not in groups:
                    groups[group] = set()

                if num in groups[group]:
                    return False
                groups[group].add(num)

        return True

                