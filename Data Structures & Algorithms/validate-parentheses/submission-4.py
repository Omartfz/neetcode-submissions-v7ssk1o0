class Solution:
    def isValid(self, s: str) -> bool:
        dico={")":"(","]":"[","}":"{"}
        stack=[]
        for k in s:
            if k in dico :
                if not stack:
                    return False
                last=stack.pop()
                if last!=dico[k]:
                    return False
            else:
                stack.append(k)
        return stack==[]
            

        