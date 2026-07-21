class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])

        directions = [[0,1],[0,-1],[1,0],[-1,0]]

        visited = set()

        def dfs(r,c):
            if r<0 or r>=rows or c<0 or c >= cols:
                return False
            op = True
            if (r,c) not in visited and board[r][c]!="X":
                visited.add((r,c))
                for dr,dc in directions:
                    op = op and dfs(r+dr,c+dc)
            
            return op



        for r in range(rows):
            for c in range(cols):
                if board[r][c]=="O":
                    visited =set()
                    if dfs(r,c):
                        for ri,ci in visited:
                            board[ri][ci]="X"
