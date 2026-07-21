class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid),len(grid[0])

        visited = set()
        directions = [[0,1],[1,0],[0,-1],[-1,0]]


        def dfs(r,c):
            if r<0 or c < 0 or r >= ROWS or c >=COLS or (r,c) in visited or grid[r][c] == 0:
                return 0
            
            visited.add((r,c))

            return 1 + dfs(r,c+1) + dfs(r+1,c) + dfs(r-1,c) +dfs(r,c-1)
        res = 0 
        for i in range(ROWS):
            for j in range(COLS):
                if (i,j) not in visited and grid[i][j]==1:
                    res = max(dfs(i,j),res)
        
        return res