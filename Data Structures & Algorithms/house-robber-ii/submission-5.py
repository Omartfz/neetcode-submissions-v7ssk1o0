class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]

        memo1=[-1]*len(nums)
        memo2=[-1]*len(nums)
        def dfs(i,num,memo):
            if i>= len(num):
                return 0
            if memo[i]!=-1:
                return memo[i]
            memo[i]=max(num[i]+dfs(i+2,num,memo),dfs(i+1,num,memo))
            return memo[i]
        num1=nums[1:]
        num2=nums[:-1]
        dfs(0,num1,memo1)
        dfs(0,num2,memo2)
        res1= max(memo1)
        res2=max(memo2)
        return max(res1,res2)   
























        """if len(nums)==1:
            return nums[0]

        rob1,rob2=0,0

        for i in range(1,len(nums)):
            temp=max(nums[i]+rob1,rob2)
            rob1=rob2
            rob2=temp
        res1=rob2
        rob1,rob2=0,0

        for i in range(len(nums)-1):
            temp=max(nums[i]+rob1,rob2)
            rob1=rob2
            rob2=temp
        res2=rob2

        return max(res2,res1)"""
