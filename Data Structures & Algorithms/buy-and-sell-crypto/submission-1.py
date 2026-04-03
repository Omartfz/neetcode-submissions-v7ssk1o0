class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        maxprice=prices[0]
        minprice=prices[0]
        res=maxprice-minprice
        left=0
        for right in range(len(prices)):
            if prices[right]<minprice:
                minprice=prices[right]
                maxprice=prices[right]
                left=right
            maxprice=max(maxprice,prices[right])
            res=max(res,maxprice-minprice)
        return res

        