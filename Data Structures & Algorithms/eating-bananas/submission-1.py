import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        speed=1
        speedmax=max(piles)
        while speed<=speedmax :
            k=(speed+speedmax)//2
            time=0
            for pile in piles:
                time +=math.ceil(pile/k)
            if time<=h:
                res=k
                speedmax=k-1
            else:
                speed=k+1

        return res
                
        
        