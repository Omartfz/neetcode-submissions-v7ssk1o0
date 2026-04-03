class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dico={}
        for x in nums : 
            if x in dico:
                dico[x]+=1
            else:
                dico[x]=1
        
        res=[]
        for i in range(k):
            cle_max=max(dico,key=dico.get)
            if dico[cle_max]>-1:
                res.append(cle_max)
            dico[cle_max]=-1
        return res
        