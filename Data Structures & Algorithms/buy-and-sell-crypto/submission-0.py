class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0,1
        max_profit = 0
        while l<len(prices)-1:
            profit = prices[r] - prices[l]
            if profit> max_profit:
                max_profit = profit
            r +=1
            if r == len(prices):
                l +=1
                r = l+1
        return max_profit
        