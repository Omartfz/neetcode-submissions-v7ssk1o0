class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def memo(r,c,rows,cols,cache):
            if r==rows or c==cols:
                return 0
            if cache[(r,c)]>0:
                return cache[(r,c)]
            if r==rows-1 and c==cols-1:
                return 1
            cache[(r,c)]=memo(r+1,c,rows,cols,cache)+memo(r,c+1,rows,cols,cache)
            return cache[(r,c)]

        dico={}
        for i in range (m):
            for j in range(n):
                dico[(i,j)]=0
        return memo(0,0,m,n,dico)











        def memo(r,c,rows,cols,cache):
            if r==rows or c==cols:
                return 0
            if cache[(r,c)]>0:
                return cache[(r,c)]
            if r==rows-1 and c==cols-1:
                return 1
            cache[(r,c)]=memo(r+1,c,rows,cols,cache)+memo(r,c+1,rows,cols,cache)
            return cache[(r,c)]
        dic={}
        for r in range (m):
            for c in range(n):
                dic[(r,c)]=0
        return memo(0,0,m,n,dic)

        