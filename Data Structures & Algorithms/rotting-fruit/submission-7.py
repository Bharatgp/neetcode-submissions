class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        q = collections.deque()
        fresh = 0
        # min - 0 

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i,j))
                    visited.add((i,j))
                if grid[i][j] == 0:
                    visited.add((i,j))
                if grid[i][j] == 1:
                    fresh += 1                    
        mins = 0
        directions = [(0,1),(0,-1),(1,0),(-1,0)] 
        while fresh>0 and q:
            qLen = len(q)
            for i in range(qLen):
                r,c = q.popleft()            
                for dr,dc in directions:
                    nr,nc = r+dr, c+dc
                    if (nr in range(rows) and nc in range(cols) and (nr,nc) not in visited):
                        fresh -= 1
                        visited.add((nr,nc))
                        q.append((nr,nc))
            mins += 1      

        return mins if fresh == 0 else -1

