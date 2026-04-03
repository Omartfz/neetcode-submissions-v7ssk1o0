class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left=[1]
        right=[1]
        n=len(nums)
        for i in range (1,len(nums)):
            left.append(left[-1]*nums[i-1])
            right.append(right[-1]*nums[n-1-i+1])
        print(left)
        print(right )
        res=[left[k]*right[n-1-k] for k in range(len(nums))]
        return res
        

        
        

        
        