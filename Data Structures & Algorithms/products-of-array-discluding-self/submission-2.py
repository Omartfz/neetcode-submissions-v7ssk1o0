class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        right=[1]*n
        left=[1]*n
        for i in range (1,len(nums)):
            left[i]=nums[i-1]*left[i-1]
        for i in range(len(nums)-2,-1,-1):
            right[i]=nums[i+1]*right[i+1]
        res=[]
        for i in range(len(nums)):
            res.append(left[i]*right[i])
        return res

        
        

        
        