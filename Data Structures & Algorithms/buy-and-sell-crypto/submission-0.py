class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # profit = cur_price - buy_price

        maxProfit = 0
        buy=prices[0]
        for i in range(1, len(prices)):
            if buy > prices[i]:
                buy = prices[i]
            
            maxProfit = max(maxProfit, prices[i]-buy)
        return maxProfit