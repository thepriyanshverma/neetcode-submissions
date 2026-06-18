class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row=[set() for _ in range(9)]
        col=[set() for _ in range(9)]
        box=[set() for _ in range(9)]
        for r in range(9):
            for c in range(9):
                num=board[r][c]
                if num=='.':
                    continue
                box_ind=(r//3)*3+(c//3)
                if num in row[r]:
                    return False
                if num in col[c]:
                    return False
                if num in box[box_ind]:
                    return False
                row[r].add(num)
                col[c].add(num)
                box[box_ind].add(num)
        return True