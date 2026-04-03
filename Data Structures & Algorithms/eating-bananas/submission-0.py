class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_rate=1
        max_rate=max(piles)
        time=float('inf')
        while max_rate>min_rate:
            mid=(max_rate+min_rate)//2
            actual_time=0
            time=sum(math.ceil(p / mid) for p in piles)
            if time>h:
                min_rate=mid+1
            else:
                max_rate=mid
            
        return min_rate
        