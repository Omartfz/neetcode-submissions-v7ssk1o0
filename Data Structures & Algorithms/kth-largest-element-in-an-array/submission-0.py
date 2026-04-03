import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        res=[]
        heapq.heapify([])
        for x in nums:
            heapq.heappush(res,x)
            if len(res)>k:
                heapq.heappop(res)
        return res[0]
        


        