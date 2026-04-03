class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo=[]
        memo.append(0)
        for i in range (len(nums)):
            nextdp=[]
            for s in memo:
                nextdp.append(s+nums[i])
                nextdp.append(s-nums[i])
            memo=nextdp
        res=0
        for s in memo:
            if s==target:
                res+=1
        return res