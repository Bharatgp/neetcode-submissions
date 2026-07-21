class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        top, bottom = 0, rows-1
        res_row = 0
        while top<=bottom:
            mid = top + (bottom-top)//2
            if(matrix[mid][0]<= target <= matrix[mid][cols-1]):
                res_row = mid
                break
            elif(matrix[mid][0] > target):
                bottom = mid - 1
            else:
                top = mid + 1                

        left, right = 0, cols-1

        while left <= right : 
            mid = left + (right-left)//2

            if(matrix[res_row][mid] == target):
                return True
            elif(matrix[res_row][mid] > target):
                right = mid - 1
            else:
                left = mid+1
        return False                                

