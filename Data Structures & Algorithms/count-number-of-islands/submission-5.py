class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited= set()
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        def dfs(r,c):
            if r<0 or r>=rows or c<0 or c>=cols or grid[r][c]=="0" or (r,c) in visited:
                return
            
            visited.add((r,c))

            for dr,dc in directions:
                nr,nc = dr+r,dc+c
                dfs(nr,nc)
        res = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=="1" and (i,j) not in visited:
                    dfs(i,j)
                    res +=1
        return res


