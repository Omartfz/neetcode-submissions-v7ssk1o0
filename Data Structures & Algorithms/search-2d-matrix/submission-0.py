class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        if not matrix or not matrix[0]:
            return False

        n, m = len(matrix), len(matrix[0])

        row_l, row_r = 0, n - 1
        row = -1

        while row_l<=row_r:
            mid=(row_l+row_r)//2
            if target< matrix[mid][0]:
                row_r=mid-1
            elif target>matrix[mid][-1]:
                row_l=mid+1
            else:
                row=mid
                break
        if row==-1:
            return False 
        nums=matrix[row]
        l=0
        r=len(nums)-1
        while l<=r:
            if nums[(r+l)//2]==target:
                return True
            elif nums[(r+l)//2]>target:
                r=(r+l)//2-1
            else:
                l=(r+l)//2+1
        return False

                










        

        l=0
        r=len(nums)-1
        while l<=r:
            if nums[(r+l)//2]==target:
                return (r+l)//2
            elif nums[(r+l)//2]>target:
                r=(r+l)//2-1
            else:
                l=(r+l)//2+1
        return -1
        