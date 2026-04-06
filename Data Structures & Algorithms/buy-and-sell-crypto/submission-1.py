class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        prices = [10,1,5,6,7,1]
        profit = cur_price - buy_price
        
        """

        buy_price = prices[0]
        maxProfit = 0
        
        for i in range(1, len(prices)):
            if buy_price > prices[i]:
                buy_price = prices[i]
            
            maxProfit = max(maxProfit, prices[i] - buy_price)
        return maxProfit