class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        INF = float('inf')
        path = k+1
        dp = [[INF] * n for _ in range(path + 1)]
        dp[0][src] = 0  

        for i in range(1, path + 1):
            dp[i] = dp[i-1].copy()
            for start, end, cost in flights:
                dp[i][end] = min(
                    dp[i][end],
                    dp[i-1][start] + cost
                )
        result = dp[path][dst]
        return result if result != INF else -1