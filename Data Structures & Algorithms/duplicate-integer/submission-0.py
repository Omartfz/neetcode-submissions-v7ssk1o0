class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dico={}
        for k in nums:
            if k in dico:
                dico[k]+=1
            else:
                dico[k]=1
            if dico[k]>1:
                return True
        return False
        

        