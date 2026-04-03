class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        if not matrix or not matrix[0]:
            return False

        n, m = len(matrix), len(matrix[0])

        row_l=0
        row_r=m-1
        row=0
        while row<n:
            while target>matrix[row][m-1] and row<n-1:
                row=row+1
            if row==n:
                return False
            while row_l<=row_r:
                mid=(row_l+row_r)//2
                if target ==matrix[row][mid]:
                    return True
                elif target<matrix[row][mid]:
                    row_r=mid-1
                else:
                    row_l=mid+1
            return False



                










        

        
        