class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if strs=="":
            return [[""]]
        dico={}
        for k in strs:
            if "".join(sorted(k)) in dico:
                dico["".join(sorted(k))].append(k)
            else:
                dico["".join(sorted(k))]=[k]
        res=[]
        for val in dico.values():
            res.append(val)
        return res

        