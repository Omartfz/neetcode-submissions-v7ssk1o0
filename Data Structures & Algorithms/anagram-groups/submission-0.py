class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dico=defaultdict(list)
        for word in strs:
            dic=[0]*26
            for k in word:
                dic[ord(k)-97]+=1

            key=tuple(dic)

            
            dico[key].append(word)
            
        res=[value for value in dico.values()]
        return res

        