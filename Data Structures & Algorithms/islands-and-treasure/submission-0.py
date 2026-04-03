class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        INF = 2147483647
        def bfs(r,c):
            visit=set()
            queue=deque()
            visit.add((r,c))
            queue.append((r,c))
            dist=0
            while queue:
                for _ in range(len(queue)):
                    r,c=queue.popleft()
                    if grid[r][c]==0:
                        return dist
                    neighbors=[[0,1],[0,-1],[1,0],[-1,0]]
                    for dr,dc in neighbors:
                        if (not(min(dc+c,dr+r)<0 or r+dr==ROWS or c+dc==COLS)) and ((r+dr,c+dc) not in visit) and (grid[dr+r][dc+c]!=-1 ) :
                            queue.append((r+dr,c+dc))
                            visit.add((r+dr,c+dc))
                dist+=1
            return INF
        for r in range (len(grid)):
            for c in range (len(grid[0])):
                if grid[r][c]==INF:
                    grid[r][c]=bfs(r,c)


