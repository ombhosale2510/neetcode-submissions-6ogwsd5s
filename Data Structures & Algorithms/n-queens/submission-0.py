class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        # 
        n*n grid, Q placement on each position, check which immediate 
        next position would be vacant

        # backtracking, we place and check other vals , append that 
        possible solution to result if True

        # 
        cols, negDiag, posDiag, sets: to track where not to place Q (skip over)

        board = ["."*n for i in range(n)]
        result.append copy if r==n


        explore other choices
        add blocks to sets
        backtrack to the next row
        remove blocks to sets

        # 
        """

        cols = set()
        negDiag = set()
        posDiag = set()
        result = []

        board = [["."]*n for i in range(n)]

        def backtrack(r):
            if r == n: # reached the last row
                result.append(["".join(row) for row in board]) # [[]]
                return
        
            for c in range(n):
                if c in cols or r-c in negDiag or r+c in posDiag:
                    continue # skip over this section, Q cannot be placed

                cols.add(c)
                negDiag.add((r-c))
                posDiag.add((r+c))
                board[r][c] = "Q"

                backtrack(r+1) # go to the next row, Q cannot be placed in the same row again

                cols.remove(c)
                negDiag.remove((r-c))
                posDiag.remove((r+c))
                board[r][c] = "."
        backtrack(0)
        return result