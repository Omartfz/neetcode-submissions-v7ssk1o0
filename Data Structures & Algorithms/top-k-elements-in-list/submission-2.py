class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dico={}
        for char in nums:
            if char in dico:
                dico[char]+=1
            else:
                dico[char]=1
        res=[]
        for i in range(k):
            cle_max = max(dico, key=dico.get)
            if dico[cle_max]>-1:
                res.append(cle_max)
            dico[cle_max]=-1

        return res

        