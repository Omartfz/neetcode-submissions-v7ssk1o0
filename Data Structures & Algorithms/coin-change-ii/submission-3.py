class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dico={}
        def dfs(i,rest):
            if rest==0:
                return 1
            if i>=len(coins) or rest<0:
                return 0
            if (i,rest) in dico:
                return dico[(i,rest)]
            skip=dfs(i+1,rest)
            no_skip=dfs(i,rest-coins[i])
            dico[(i,rest)]=skip+no_skip
            return dico[(i,rest)]
        return dfs(0,amount)