class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # sliding window left right pointer
        # it will work such that fix the left on one end and move the right until the left is greater repplace it with the right and again fix it there and move the right again but right should not cross the length of the total

        lp, rp = 0, 1
        max_profit = 0

        while rp < len(prices):
            if prices[lp] < prices[rp]:
                current_profit = prices[rp] - prices[lp]
                max_profit = max(max_profit, current_profit)
            else:
                lp = rp
            rp+=1
        
        return max_profit
