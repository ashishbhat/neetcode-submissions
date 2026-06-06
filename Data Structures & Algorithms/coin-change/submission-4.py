class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def helper(coins: List[int], amount: int, cache: dict = None):
            if cache is None:
                cache = {}
            if amount == 0:
                return 0
            elif amount < 0:
                return float('inf')
            elif amount in cache:
                return cache[amount]

            cache[amount] = min([1 + helper(coins, amount - coin, cache) for coin in coins])
            return cache[amount]
        
        best = helper(coins, amount)
        return best if best != float('inf') else -1
        
            
