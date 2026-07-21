class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        wi=0
        ROWS, COLS = len(board), len(board[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        visited = set()
        def helper(r,c,word,visited,wi):
            if wi == len(word) :
                return True
            if(r not in range(ROWS) or c not in range(COLS) or (r,c)  in visited or board[r][c] != word[wi]):
                return False
            visited.add((r,c))
           
            res = (helper(r+1,c,word,visited,wi+1) or
            helper(r-1,c,word,visited,wi+1) or
            helper(r,c+1,word,visited,wi+1) or
            helper(r,c-1,word,visited,wi+1))

            visited.remove((r,c))

            return res         
            
        for i in range(ROWS):
            for j in range(COLS):
                if(word[0]==board[i][j]):
                    if(helper(i,j,word,visited,0)):
                        return True
        return False
        

                
