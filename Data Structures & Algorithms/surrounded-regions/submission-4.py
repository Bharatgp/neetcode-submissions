class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS,COLS = len(board), len(board[0])
        visited = set()
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        def dfs(r,c):
            if(r in range(ROWS) and c in range(COLS) and board[r][c]=="O" and (r,c) not in visited):
                board[r][c]="Y"
                visited.add((r,c))
                for dr,dc in directions:
                    nr,nc = r+dr, c+dc
                    dfs(nr,nc)

                
        for r in range(ROWS):
            for c in range(COLS):
                if((r==0 or c==0 or r==ROWS-1 or c==COLS-1) and board[r][c]=="O"):
                    dfs(r,c)
        for r in range(ROWS):
            for c in range(COLS):
                if(board[r][c]=="O"):
                    board[r][c]="X"
                if(board[r][c]=="Y"):
                    board[r][c]="O"

                
