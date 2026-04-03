class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        curset,res=[],[]
        self.helper(0,nums,curset,res)
        return res

    def helper(self,i,nums,curset,res):
        if i>=len(nums):
            
            if curset not in res:
                res.append(curset.copy())
            return res
        curset.append(nums[i])
        
        self.helper(i+1,nums,curset,res)
        curset.pop()
        self.helper(i+1,nums,curset,res)
        