class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        rows, cols = len(grid),len(grid[0])
        visited = set()
        q = collections.deque()
        directions = [[0,1],[0,-1],[-1,0],[1,0]]
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c]==2:
                    q.append((r,c))
        time = 0
        while q and fresh > 0:
            lenq = len(q)

            for i in range(lenq):
                rr,rc = q.popleft()
                for dr,dc in directions:
                    nr,nc = rr+dr, rc+dc
                    if(nr>=0 and nc>=0 and nr<rows and nc<cols and grid[nr][nc]==1):
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr,nc))
            time += 1
        
        return -1 if fresh!=0 else time
            
    