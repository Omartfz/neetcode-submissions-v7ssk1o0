class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum=nums[0]
        cursum=0
        for i in range(len(nums)):
            cursum=max(cursum,0)
            cursum+=nums[i]
            maxsum=max(cursum,maxsum)
        
        return maxsum


        