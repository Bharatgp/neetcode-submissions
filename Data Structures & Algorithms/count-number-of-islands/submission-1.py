class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        islandCount = 0
        def visitIsland(r,c):
            visited.add((r,c))
            for dr,dc in directions:
                nr,nc = r + dr, c + dc

                if(nr in range(ROWS) and nc in range(COLS) and (nr,nc) not in visited and grid[nr][nc] == "1"):
                    visitIsland(nr,nc)

        for r in range(ROWS):
            for c in range(COLS):
                if(grid[r][c] == "1" and (r,c) not in visited):
                    visitIsland(r,c)
                    islandCount += 1
        return islandCount