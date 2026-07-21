class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        area = 0
        
        def islandArea(r,c):
            
            if(r in range(ROWS) and c in range(COLS) and (r,c) not in visited and grid[r][c] == 1):
                visited.add((r,c))
                return 1 + islandArea(r,c+1) + islandArea(r,c-1) + islandArea(r + 1,c) + islandArea(r-1,c)
            return 0                
            


        for r in range(ROWS):
            for c in range(COLS):
                if(grid[r][c] == 1 and (r,c) not in visited):
                    area = max(area, islandArea(r,c))
        return area