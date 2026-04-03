class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        curset,res=[],[]
        self.helper(0,nums,curset,res)
        return res
    def helper(self,i,nums,curset,res):
        if i>=len(nums):
            res.append(curset.copy())
            return
        curset.append(nums[i])
        self.helper(i+1,nums,curset,res)
        curset.pop()
        self.helper(i+1,nums,curset,res)

        