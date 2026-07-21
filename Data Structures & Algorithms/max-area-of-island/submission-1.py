class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visit = set()
        res = []
        directions = [[0,1],[0,-1],[1,0],[-1,0]]

        def bfs(r, c) -> int:
            q = collections.deque()
            q.append((r, c))
            visit.add((r, c))
            area = 1    
            while q:
                print(q)
                row, col = q.popleft()
                for dr, dc in directions:
                    r1, c1 = row + dr, col + dc
                    print(dr, dc)
                    print(r1, c1)
                    if(r1 in range(rows) and c1 in range(cols) and grid[r1][c1] == 1 and (r1,c1) not in visit):
                        visit.add((r1, c1))
                        q.append((r1, c1))
                        area += 1

            return area


        for r in range(rows):
            for c in range(cols):
                if(grid[r][c] == 1 and (r, c) not in visit):
                    print("Hi")
                    print(r,c)
                    i = bfs(r, c)
                    res.append(i)
        if res:                      
            return max(res)
        return 0    