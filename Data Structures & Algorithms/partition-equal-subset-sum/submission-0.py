class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        T = sum(nums)
        if T % 2 == 1:
            return False
        N = len(nums)
        T = T//2

        dp = [ [False] * (N+1) for _ in range(T + 1)]
        dp[0][0] = True

        for i in range(0, T+1):
            for j in range(1, N+1):
                if i == j == 0:
                    continue
                current = nums[j - 1]
                if i >= current:
                    dp[i][j] = dp[i - current][j-1] or dp[i][j-1]
                else:
                    dp[i][j] = dp[i][j-1]

        return dp[T][N]
