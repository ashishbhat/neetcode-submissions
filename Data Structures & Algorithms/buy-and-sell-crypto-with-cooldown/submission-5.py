class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        def backtrack(day: int, coin: int) -> int:
            if day >= len(prices):
                return 0
            if (day, coin) in dp:
                return dp[(day, coin)]
            
            p = 0
            # buy
            if not coin:
                p = backtrack(day+1, prices[day])

            # don't buy
            p = max(p, backtrack(day+1, coin))

            # sell
            if coin is not None and prices[day] > coin:
                p = max(p, prices[day] - coin + backtrack(day+2, None))
            dp[(day, coin)] = p
            return p

        return backtrack(0, None)