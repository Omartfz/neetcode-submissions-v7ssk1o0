class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        minprice=prices[0]
        res=0
        for p in prices:
            if p<minprice:
                minprice=p
            else:
                res=max(res,p-minprice)
        return res

        