class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit: int = 0
        buy_price = prices[0]
        for current_price in prices:
            buy_price = min(current_price, buy_price)
            max_profit = max(max_profit, current_price - buy_price)
        return max_profit


            