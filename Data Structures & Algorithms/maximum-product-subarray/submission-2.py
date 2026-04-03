class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product=nums[0]
        min_product=nums[0]
        res=nums[0]
        for i in range(1,len(nums)):
            curr_max=max_product
            max_product=max(max_product*nums[i],nums[i],min_product*nums[i])
            min_product=min(min_product*nums[i],nums[i],curr_max*nums[i])
            res=max(res,max_product)
        return res

        