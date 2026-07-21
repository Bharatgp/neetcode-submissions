class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        wi=0
        ROWS, COLS = len(board), len(board[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        visited = set()
        def helper(r,c,word,visited,wi):
            if wi == len(word) :
                return True
            for dr,dc in directions:
                nr,nc = r+dr, c+dc
                if(nr in range(ROWS) and nc in range(COLS) and (nr,nc) not in visited):
                    if(board[nr][nc]==word[wi]):
                        visited.add((nr,nc))
                        if (helper(nr,nc,word,visited,wi+1)):
                            return True
                        visited.remove((nr,nc))
            return False    
            
        for i in range(ROWS):
            for j in range(COLS):
                if(word[0]==board[i][j]):
                    visited.add((i,j))
                    if(helper(i,j,word,visited,1) == True):
                        return True
                    visited.remove((i,j))                        
        return False