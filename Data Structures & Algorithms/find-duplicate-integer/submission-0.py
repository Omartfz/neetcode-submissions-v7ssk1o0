class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dico={}
        for k in nums:
            if k in dico:
                return k
            else:
                dico[k]=1
        