class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buyidx = 0
        sellidx = None
        for i in range(1, len(prices)):
            if prices[i] < prices[buyidx]:
                buyidx = i
                continue
            curr_profit = prices[i] - prices[buyidx]
            if curr_profit > max_profit:
                max_profit = curr_profit
                sellidx = i
        return max_profit



        