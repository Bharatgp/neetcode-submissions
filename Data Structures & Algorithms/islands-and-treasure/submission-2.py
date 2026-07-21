class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        q = collections.deque()
        visited = set()
        for r in range(rows):
            for c in range(cols):
                if(grid[r][c]==0):
                    q.append((r,c))
                    visited.add((r,c))
        dis = 0
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        while q:
            qLen = len(q)
            for i in range(qLen):
                curr_cell= q.popleft()
                grid[curr_cell[0]][curr_cell[1]] = dis
                for dr,dc in directions:
                    nr,nc = curr_cell[0]+dr, curr_cell[1]+dc
                    if( nr>=0 and nc>=0 and nr<rows and nc < cols and (nr,nc) not in visited and grid[nr][nc]!= -1):
                        q.append((nr,nc))
                        visited.add((nr,nc))
            dis+=1

                        


        

