class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        time = 0
        fresh = 0
        q = deque()

        # count fresh and add rotten to queue
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh+=1
                if grid[r][c] == 2:
                    q.append([r, c])
        
        while q and fresh > 0:
            # process fruits by level
            for i in range(len(q)):
                row, col = q.popleft()

                directions = [(0,1), (0,-1), (1,0), (-1,0)]
                for dr, dc in directions:
                    r, c = dr+row, dc+col

                    if r<0 or r>=ROWS or c<0 or c>=COLS or grid[r][c] != 1: 
                        continue
                    grid[r][c] = 2
                    fresh-=1
                    q.append([r, c])
            time+=1
        return time if fresh == 0 else -1