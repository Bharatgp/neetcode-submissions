class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        fresh = 0
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        visited = set()
        mins = 0
        for r in range(ROWS):
            for c in range(COLS):
                if(grid[r][c] == 2):
                    q.append((r,c))
                    visited.add((r,c))                    
                if(grid[r][c] == 1):
                    fresh += 1
        while q and fresh > 0:
            qlen = len(q)
            for i in range(qlen):
                r,c = q.popleft()
                grid[r][c]=2
                for dr,dc in directions:
                    nr,nc = r+dr, c+dc
                    if(nr in range(ROWS) and nc in range(COLS) and (nr,nc) not in visited and grid[nr][nc]==1):
                        q.append((nr,nc))
                        visited.add((nr,nc))
                        fresh -= 1
            mins += 1                                   
        return mins if fresh == 0 else -1                          


