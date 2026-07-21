class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix) - 1
        COLS = len(matrix[0]) - 1 
        l,r = 0, ROWS
        target_row = 0
        while(l<=r):
            m = (l+r)//2
            if(matrix[m][0]<= target <=matrix[m][COLS]):
                target_row = m
                break
            elif(target<matrix[m][0]):
                r = m - 1
            else:
                l = m + 1
        l,r = 0, COLS
        while(l<=r):
            m = (l+r)//2
            if(matrix[target_row][m]==target):
                return True
            elif(matrix[target_row][m]<target):
                l = m + 1
            else:
                r = m - 1
        return False                                                                            

