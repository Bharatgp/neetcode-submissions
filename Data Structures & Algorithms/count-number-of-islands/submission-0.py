class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
           return 0
        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = 0

        def bfs(r, c):
            q = collections.deque()
            q.append((r, c))
            directions = [[0,1],[0,-1],[1,0],[-1,0]]
            while q:
                r,c = q.popleft()
                for row, col in directions:
                    rw,co = r + row, c + col
                    if (rw in range(rows) and 
                        co in range(cols) and 
                        grid[rw][co] == "1" and 
                        (rw, co) not in visit):
                        q.append((rw,co))
                        visit.add((rw,co))
                        
            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(r, c)
                    visit.add((r, c))
                    islands += 1
        return islands
                