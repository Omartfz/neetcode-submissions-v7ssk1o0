import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        occurence={x:0 for x in tasks}
        for x in tasks:
            occurence[x]+=1
        maxHeap=[-cnt for cnt in occurence.values()]
        heapq.heapify(maxHeap)
        time=0
        q=deque()
        while maxHeap or q:
            time+=1
            if not maxHeap:
                time=q[0][1]
            else:
                cnt=1+heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt,time+n])
            if q and q[0][1]==time:
                heapq.heappush(maxHeap,q.popleft()[0])
        return time



        
        