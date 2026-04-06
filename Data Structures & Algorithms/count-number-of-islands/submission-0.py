class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # horizontally or vertically, NOT diagonally

        """
        Input: grid = [
            ["1","1","0","0","1"],
            ["1","1","0","0","1"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]
        ]
        Output: 4
        """

        ROWS, COLS = len(grid) , len(grid[0])
        visited = set()
        islands = 0

        def bfs(r,c):
            q = deque([(r,c)])
            
            visited.add((r,c))

            while q:
                row, col = q.popleft()

                directions = [(0,1),(1,0),(-1,0),(0,-1)]

                for dr, dc in directions:
                    nr, nc = row+dr, col+dc

                    if ROWS>nr>=0 and COLS>nc>=0 and grid[nr][nc] == "1" and (nr,nc) not in visited:
                        q.append((nr, nc))
                        visited.add((nr, nc))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    islands+=1
                    
        return islands
        