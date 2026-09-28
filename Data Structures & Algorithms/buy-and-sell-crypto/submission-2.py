class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # sliding window left right pointer
        lp, rp = 0, 1
        max_profit = 0

        while rp < len(prices):
            
            if prices[lp] < prices[rp]:
                profit = prices[rp]-prices[lp]
                max_profit = max(max_profit, profit)
            else:
                lp = rp
            rp+=1

        return max_profit