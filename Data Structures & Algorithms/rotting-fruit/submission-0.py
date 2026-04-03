class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        fresh=0
        time=0
        queue=deque()
        for r in range (len(grid)):
            for c in range (len(grid[0])):
                if grid[r][c]==1:
                    fresh+=1
                if grid[r][c]==2:
                    queue.append((r,c))
        while queue and fresh>0:
            for i in range (len(queue)):
                r,c=queue.popleft()
                for dr, dc in directions:
                    row,col=r+dr,c+dc
                    if (not(min(dc+c,dr+r)<0 or r+dr==ROWS or c+dc==COLS)) and grid[row][col]==1:
                        grid[row][col]=2
                        queue.append((row,col))
                        fresh+=-1
            time+=1
        return time if fresh ==0 else-1


        