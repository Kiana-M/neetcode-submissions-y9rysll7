class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # idea: keep track of the lowest price and max profit
        # only calculate profit if you encounter a new lowest because 
        # only in that case will you gain higher profit
        max_profit, r, lowest = 0, 0, prices[0]

        for r in range(len(prices)):
            max_profit = max(max_profit, prices[r]-lowest)
            if prices[r]<lowest:
                lowest = prices[r]

        return max_profit

        
        
        