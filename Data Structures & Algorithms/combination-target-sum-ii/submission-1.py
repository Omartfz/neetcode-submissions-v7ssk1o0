class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        curset,res=[],[]
        candidates.sort()
        self.helper(0,candidates,curset,res,target,0)
        return res
    def helper(self,i,nums,curset,res,target,cursum):
        if cursum==target:
            res.append(curset.copy())
            return
        if i>=len(nums) or cursum>target:
            return
        curset.append(nums[i])
        self.helper(i+1,nums,curset,res,target,cursum+nums[i])
        while i<len(nums)-1 and nums[i+1]==nums[i]:
            i+=1
        curset.pop()
        self.helper(i+1,nums,curset,res,target,cursum)