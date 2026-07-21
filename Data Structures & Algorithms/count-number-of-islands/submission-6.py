class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS,COLS = len(grid), len(grid[0])
        visited = set()
        directions = [[0,1],[1,0],[-1,0],[0,-1]]

        def dfs(r,c):
            
            if r<0 or r>= ROWS or c < 0 or c >= COLS or (r,c) in visited or grid[r][c]=='0':
                return 
            visited.add((r,c))
            for dr,dc in directions:
                nr,nc = r+dr, c+dc
                dfs(nr,nc)
        res = 0
        for i in range(ROWS):
            for j in range(COLS):
                if (i,j) not in visited and grid[i][j] == '1':
                    dfs(i,j)
                    res += 1
        return res

