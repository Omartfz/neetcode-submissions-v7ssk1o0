class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dico={}
        for i in range(len(nums)):
            val=target-nums[i]
            if nums[i] in dico and dico[nums[i]]!=i:
                return [dico[nums[i]],i]
            else:
                dico[val]=i
            