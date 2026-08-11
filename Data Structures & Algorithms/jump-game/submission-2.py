class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo={}
        def dfs(i):
            if i==len(nums)-1:
                return True
            elif nums[i]==0:
                return False 
            if i in memo:
                return memo[i]
            else:
                res=False
                for j in range(1,nums[i]+1):
                    if i+j<=len(nums)-1:
                        res=dfs(i+j) or res
                memo[i]=res
            return memo[i]
        return dfs(0)
