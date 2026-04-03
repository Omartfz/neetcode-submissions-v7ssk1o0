import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances=[]
        for i in range(len(points)):
            distance=math.sqrt(points[i][0]**2+points[i][1]**2)
            distances.append((distance,points[i]))
        heapq.heapify(distances)
        res=[]
        cpt=0
        for _ in range (k):
            last=heapq.heappop(distances)
            res.append(last[1])
        return res
        