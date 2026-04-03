class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        dic_s={}
        dic_t={}
        for car in s:
            if car in dic_s:
                dic_s[car]+=1
            else:
                dic_s[car]=1
        for car in t:
            if car in dic_t:
                dic_t[car]+=1
            else:
                dic_t[car]=1
        for key in dic_t:
            if key not in dic_s:
                return False
            elif dic_s[key]!=dic_t[key]:
                return False
        return True


        

        