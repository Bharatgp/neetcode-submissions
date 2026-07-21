class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        visited = set()

        def dfs(r,c):
            if(r<0 or c<0 or c>=COLS or r>= ROWS or grid[r][c]==0 or (r,c) in visited):
                return 0
            visited.add((r,c))                
            return (1 + dfs(r,c+1) + dfs(r,c-1) + dfs(r-1,c) + dfs(r+1,c))
        area = 0
        for r in range(ROWS):
            for c in range(COLS):
                area = max(area, dfs(r,c))
        return area                    
