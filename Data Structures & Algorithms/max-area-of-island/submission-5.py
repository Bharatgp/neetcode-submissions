class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0

        rows,cols = len(grid),len(grid[0])
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        visited= set()
        area = 0
        def dfs(r,c):
            nonlocal area

            if r<0 or r>=rows or c<0 or c>=cols or (r,c) in visited or grid[r][c]==0:
                return
            area+=1
            visited.add((r,c))
            for dr,dc in directions:
                nr,nc = r+dr, c+dc
                dfs(nr,nc)
        
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and grid[r][c]==1:
                    area = 0
                    dfs(r,c)
                    maxArea = max(area,maxArea)
        return maxArea