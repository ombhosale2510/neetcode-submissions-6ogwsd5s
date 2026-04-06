class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        # U
        supposed to find if word can and does exist in the board or not
        do dfs, backtracking to check each cell, 
        somewhat like number of islands ig ?

        # M
        backtracking, 
        seen set to keep track of the current list of chars seen or 
        made so far 

        # P


        """
        ROWS, COLS = len(board), len(board[0])
        seen = set()

        def backtrack(r, c, i):
            if i == len(word):
                return True
            if  r<0 or r>=ROWS or c<0 or c>=COLS or board[r][c] != word[i] or (r, c) in seen:
                return False
            
            # if we had a match with board[r][c] == word[i], 
            # we move to next letter in word i+1

            seen.add((r, c))
            result = backtrack(r+1, c, i+1) or backtrack(r-1, c, i+1) or backtrack(r, c+1, i+1) or backtrack(r, c-1, i+1) 
            seen.remove((r, c))
            
            return result

        for r in range(ROWS):
            for c in range(COLS):
                if backtrack(r, c, 0): # index is for word[i]
                    return True
        return False