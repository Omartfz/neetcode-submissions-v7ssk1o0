class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2:
            return False
        memo=set()
        memo.add(0)
        target=sum(nums)//2
        for i in range (len(nums)-1,-1,-1):
            nextdp=set()
            for t in memo:
                nextdp.add(t)
                nextdp.add(t+nums[i])
            memo=nextdp
        if target in memo:
            return True
        else: 
            return False
        


        