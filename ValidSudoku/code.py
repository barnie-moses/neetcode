class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(len(board))]
        cols = [set() for _ in range(len(board))]
        square = [set() for _ in range(len(board))]


        for r in range(len(board)):
            for c in range(len(board)):
                if board[r][c] == '.':
                    continue
                if (board[r][c] in rows[r] or 
                   board[r][c] in cols[c] or 
                   board[r][c] in square[(r//3)*3 + c//3]):
                   return False
                
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                square[(r//3)*3 + c//3].add(board[r][c])
        
        return True



