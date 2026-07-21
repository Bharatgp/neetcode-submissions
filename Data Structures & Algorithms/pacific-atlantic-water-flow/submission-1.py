class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        def dfs(r , c, visited, prevHeight):
            if(r in range(ROWS) and c in range(COLS) and (r,c) not in visited and heights[r][c] >= prevHeight):
                visited.add((r,c))
                for dr,dc in directions:
                    nr,nc = r+dr, c + dc
                    dfs(nr,nc,visited,heights[r][c])                


        for r in range(ROWS):
            dfs(r,0,pac,heights[r][0])
            dfs(r,COLS-1,atl,heights[r][COLS-1])            
        for c in range(COLS):
            dfs(0,c,pac,heights[0][c])
            dfs(ROWS-1,c,atl,heights[ROWS-1][c])   
        res = []     
        for r in range(ROWS):
            for c in range(COLS):
                if((r,c) in pac and (r,c) in atl):
                    res.append([r,c])
        return res