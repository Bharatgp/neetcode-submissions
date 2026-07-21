class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for i in range(n)]
        res = []

        def placeQueen(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n):
                if self.canPlace(board.copy(),r,c,n) :
                    board[r][c]='Q'
                    placeQueen(r+1)
                    board[r][c]='.'
        placeQueen(0)
        return res
    def canPlace(self,board,r,c,n):
        for i in range(n):
            if(board[r][i]=='Q' or board[i][c]=='Q'):
                return False
        x,y = r,c
        while x>=0 and y<n:
            if(board[x][y]=='Q'):
                return False
            x-=1
            y+=1                
        x,y = r,c
        while y>=0 and x<n:
            if(board[x][y]=='Q'):
                return False
            x+=1
            y-=1
        x,y = r,c
        while x>=0 and y>=0:
            if(board[x][y]=='Q'):
                return False
            x-=1
            y-=1
        x,y = r,c
        while x<n and y<n:
            if(board[x][y]=='Q'):
                return False
            x+=1
            y+=1          
        return True