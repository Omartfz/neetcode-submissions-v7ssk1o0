class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1
        while left<=right:
            if target==nums[(right+left)//2]:
                return (right+left)//2
            elif target<nums[(right+left)//2]:
                right=(right+left)//2 -1
            else:
                left=(right+left)//2+1
        return -1