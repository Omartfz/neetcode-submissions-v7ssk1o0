class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits=="":
            return []
        res=[]
        digToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        def dfs(i,curStr):
            
            if len(curStr)==len(digits):
                res.append("".join(curStr))
                return
            for j in range (len(digToChar[digits[i]])):
                curStr.append(digToChar[digits[i]][j])
                dfs(i+1,curStr.copy())
                curStr.pop()
            return
        dfs(0,[])
        return res
