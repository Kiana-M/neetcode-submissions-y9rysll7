class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #If the price at r is higher than at l, we can make a profit — so we update the maximum.
        #If the price at r is lower, then r becomes the new l because a cheaper buying price is always better.
        buy, sell, max_profit = 0, 1, 0
        while sell<len(prices):
            if prices[sell] - prices[buy] > max_profit:
                max_profit = prices[sell] - prices[buy]
            if prices[sell] - prices[buy] < 0:
                buy = sell
            sell+=1
        
        return max_profit

        
        