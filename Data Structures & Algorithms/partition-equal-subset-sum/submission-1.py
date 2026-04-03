class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s=sum(nums)
        if s%2!=0:
            return False
        t=s//2
        subset=[]
        memo=[[-1]*(t+1) for _ in range(len(nums)+1)]
        def dfs(i,t):
            if t==0:
                return True
            if i>=len(nums) or t<0:
                return False
            if memo[i][t]!=-1:
                return memo[i][t]
            memo[i][t]=dfs(i+1,t-nums[i]) or dfs(i+1,t)
            return memo[i][t]
        return dfs(0,t)