class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dico={}
        left=0
        res=0
        for i in range(len(s)):
            if s[i] in dico:
                dico[s[i]]+=1
            else:
                dico[s[i]]=1
            while (((i-left+1)-max(dico.values()))>k):
                dico[s[left]]-=1
                left+=1
            res=max(res,(i-left)+1)
        return res




        



        