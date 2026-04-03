class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)<=1:
            return False
        if not s:
            return true
        stack=[]
        dico={')':'(','}':'{',']':'['}
        for k in s:
            if k in dico:
                if not stack:
                    return False
                else:
                    last=stack.pop()
                if dico[k]!=last:
                    return False
            elif k in dico.values():
                stack.append(k)
            
        return stack==[]

        