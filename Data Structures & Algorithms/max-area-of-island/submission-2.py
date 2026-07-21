class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        area = 0

        def bfs(r,c):
            q = deque()
            q.append((r,c))
            res = 1
            grid[r][c] = 0

            while q:
                cr,cc = q.popleft()
                for dr,dc in directions:
                    nr,nc = cr + dr, cc + dc
                    if(nr<0 or nc<0 or nr >= ROWS or nc == COLS or grid[nr][nc]==0):
                        continue
                    q.append((nr,nc))
                    res+=1
                    grid[nr][nc]=0
            return res            



        for r in range(ROWS):
            for c in range(COLS):
                if(grid[r][c]==1):
                    area = max(area,bfs(r,c))
        return area