class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buy = float("inf")
        profit = 0
        max_profit = 0

        for price in prices:
            if price < buy:
                buy = price
            
            profit = price - buy
            if profit > max_profit:
                max_profit = profit
                profit = 0
        
        return max(profit,max_profit)