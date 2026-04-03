class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n,m=len(board),len(board[0])
        def dfs(board,r,c,i,visit,word):
            if min(r,c)<0 or r==n or m==c or (r,c) in visit or board[r][c]!=word[i]:
                return False
            if i==len(word)-1:
                return True
            visit.add((r,c))
            res= dfs(board,r+1,c,i+1,visit,word) or dfs(board,r-1,c,i+1,visit,word) or dfs(board,r,c-1,i+1,visit,word) or dfs(board,r,c+1,i+1,visit,word)
            visit.remove((r,c))
            return res

        for r in range(n):
            for c in range(m):
                if dfs(board,r, c, 0,set(),word):
                    return True
        return False