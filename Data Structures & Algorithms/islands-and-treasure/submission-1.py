class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        q = deque()
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        for r in range(ROWS):
            for c in range(COLS):
                if(grid[r][c]==0):
                    q.append((r,c))
                    visited.add((r,c))
        distance = 0                    
        while q:
            qlen = len(q)
            for i in range(qlen):
                r,c = q.popleft()
                grid[r][c] = distance
                for dr,dc in directions:
                    nr,nc = r+dr, c+dc
                    if(nr in range(ROWS) and nc in range(COLS) and (nr,nc) not in visited and grid[nr][nc]!=-1):
                        q.append((nr,nc))
                        visited.add((nr,nc))
            distance += 1                        



