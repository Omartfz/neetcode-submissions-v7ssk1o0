class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dico={}
        def dfs(i,j):
            if i>=m or j>=n:
                return 0
            if i==m-1 and j==n-1:
                return 1
            if (i,j) in dico:
                return dico[(i,j)]
            bottom,right=dfs(i+1,j),dfs(i,j+1)
            dico[(i,j)]=bottom+right
            return dico[(i,j)]
        return dfs(0,0)
            

        