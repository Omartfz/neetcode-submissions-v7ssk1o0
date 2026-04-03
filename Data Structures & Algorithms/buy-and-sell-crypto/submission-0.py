class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        left=0
        profit=0
        for right in range(1,len(prices)):
            if prices[right]<prices[left]:
                left=right
            else:
                profit=max(profit,prices[right]-prices[left])
        return profit

        