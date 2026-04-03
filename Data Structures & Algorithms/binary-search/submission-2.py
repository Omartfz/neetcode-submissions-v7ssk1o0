class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1
        while left<=right:
            res=(left+right)//2
            if nums[res]==target:
                return res
            elif nums[res]>=target:
                right=res-1
            else:
                left=res+1
        return -1