class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        # 1. convert border O to T (temporary)
            dfs, recursion to check surrounded region
            
            capture within a region, board - border(edges)
        """
        ROWS, COLS = len(board), len(board[0])

        def capture(r,c):
            if r<0 or c<0 or r == ROWS or c == COLS or board[r][c]!="O":
                return
            board[r][c] = "T"
            capture(r+1,c)
            capture(r-1,c)
            capture(r,c+1)
            capture(r,c-1)

            
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r in [0, ROWS-1] or c in [0, COLS-1]):
                    capture(r,c)
        
        
        
        """
        # 2. convert all O's to X
           2x for loop' goes through every O -> X
                board[r][c] = "O" then "X" 
        """
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"        
        
        """
        # 3. convert all T's back to O
           2x for loop' goes through every T -> X
                board[r][c] = "T" then "X"
        """
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"