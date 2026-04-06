class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """
        fill (INF) - land: distance to its nearest chest (0)
        
        [[2147483647,   -1,         0,          2147483647], 
        [2147483647,    2147483647, 2147483647, -1],
        [2147483647,    -1,         2147483647, -1],
        [0,             -1,         2147483647, 2147483647]]
        
        # BFS shortes path algo
        keep grid, move in directions

        """

        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        q = deque()

        def addRoom(r,c):
            if r<0 or r==ROWS or c<0 or c==COLS or (r,c) in visited or grid[r][c]==-1:
                return
            visited.add((r,c))
            q.append([r,c])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r,c])
                    visited.add((r,c))

        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()

                # gate will be 0
                grid[r][c] = dist

                addRoom(r+1,c)
                addRoom(r,c+1)
                addRoom(r-1,c)
                addRoom(r,c-1)
            dist+=1
            
