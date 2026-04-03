class Solution:
    def search(self, nums: List[int], target: int) -> int:
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