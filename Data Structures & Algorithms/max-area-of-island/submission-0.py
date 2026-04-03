class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS,COLS=len(grid),len(grid[0])
        visit=set()
        queue=deque()
        res=0
        def bfs(r,c):
            surface=0
            
            queue.append((r,c))
            visit.add((r,c))
            while queue:
                for i in range(len(queue)):
                    r,c=queue.popleft()
                    surface+=1 
                    neighbors=[[0,1],[0,-1],[1,0],[-1,0]]
                    for dr,dc in neighbors:
                        if (not(min(dc+c,dr+r)<0 or r+dr==ROWS or c+dc==COLS)) and ((r+dr,c+dc) not in visit) and (grid[dr+r][dc+c]==1) :
                            queue.append((r+dr,c+dc))
                            visit.add((r+dr,c+dc))
                            
            return surface
        for r in range (len(grid)):
            for c in range (len(grid[0])):
                if grid[r][c]==1 and (r,c) not in visit:
                    surface=bfs(r,c)
                    res=max(res,surface)
        return res
        
        