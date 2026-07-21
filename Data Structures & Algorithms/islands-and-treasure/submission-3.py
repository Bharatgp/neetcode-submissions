class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        directions = [[0,1],[0,-1],[-1,0],[1,0]]
        visited = set()
        q = collections.deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==0:
                    q.append((r,c))
                    visited.add((r,c))
        dis = 0
        while q:
            qLen = len(q)
            dis+=1
            for i in range(qLen):
                r,c = q.popleft()
                for dr,dc in directions:
                    nr,nc = r+dr, c+dc
                    if not( nr<0 or nr>=rows or nc<0 or nc>=cols or grid[nr][nc]==-1 or (nr,nc) in visited):
                        grid[nr][nc] = dis
                        q.append((nr,nc))
                        visited.add((nr, nc))
        
                    




