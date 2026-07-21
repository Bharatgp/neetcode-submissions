class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        #get the row

        low_r = 0
        high_r = ROWS-1
        r = 0
        while(low_r <= high_r):
            mid = low_r + ((high_r-low_r)//2)

            if(matrix[mid][0] <= target and matrix[mid][COLS-1] >= target):
                r = mid
                break
            elif(matrix[mid][0] > target):
                high_r = mid - 1
            else:
                low_r = mid + 1                
        low = 0
        high = COLS-1
        while(low <= high):
            m = low + ((high - low)//2)
            if(matrix[r][m]==target):
                return True
            elif(matrix[r][m]>target):
                high = m - 1
            else:
                low = m + 1
        return False                                                                