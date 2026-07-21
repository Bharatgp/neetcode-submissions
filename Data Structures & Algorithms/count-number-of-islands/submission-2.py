class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [(0,1),(0,-1),(-1,0),(1,0)]
        def dfs(i,j):
            if(i < 0 or i >= ROWS or j<0 or j>=COLS or grid[i][j]=="0"):
                return
            grid[i][j]="0"
            for r,c in directions:
                nr,nc = i+r, j+c
                dfs(nr,nc)
        res = 0
        for i in range(ROWS):
            for j in range(COLS):
                if(grid[i][j]=="1"):
                    dfs(i,j)
                    res+=1
        return res