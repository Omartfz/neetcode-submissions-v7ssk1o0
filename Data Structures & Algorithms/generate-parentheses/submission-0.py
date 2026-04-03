class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack=[("",0,0)]
        res=[]
        while stack:
            s,opened,closed=stack.pop()
            if len(s)==2*n:
                res.append(s)
                continue
            if closed<opened:
                stack.append((s+')',opened,closed+1))
            if opened<n:
                stack.append((s+'(',opened+1,closed))
            
        return res
            



