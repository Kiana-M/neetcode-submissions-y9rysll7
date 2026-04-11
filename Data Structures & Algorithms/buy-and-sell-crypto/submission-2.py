class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # l, r = 0,1
        # max_profit = 0
        # while r<len(prices):
        #     profit = prices[r] - prices[l]
        #     if profit> 0:
        #         max_profit = max(max_profit, profit)
        #     else:
        #         l = r
        #     r +=1
        # return max_profit
        max_profit, r, lowest = 0, 0, prices[0]

        for r in range(len(prices)):
            max_profit = max(max_profit, prices[r]-lowest)
            if prices[r]<lowest:
                lowest = prices[r]

        return max_profit

        
        
        