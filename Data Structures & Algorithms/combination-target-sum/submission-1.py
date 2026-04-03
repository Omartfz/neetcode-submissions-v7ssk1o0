class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        curset,res=[],[]
        self.helper(0,nums,curset,res,target,0)
        return res
    def helper(self,i,nums,curset,res,target,cursum):
        if cursum==target:
            res.append(curset.copy())
            return
        if i>=len(nums) or cursum>target:
            return
        curset.append(nums[i])
        self.helper(i,nums,curset,res,target,cursum+nums[i])
        curset.pop()
        self.helper(i+1,nums,curset,res,target,cursum)
        