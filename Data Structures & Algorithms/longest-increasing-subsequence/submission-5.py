class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [1] * N

        for i in range(N):
            for j in range(i-1, -1, -1):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], 1 + dp[j])
                    
        idx = max(range(len(dp)), key=lambda i: dp[i])
        trace = []
        current = idx
        trace.append(idx)

        for i in range(N-1, -1, -1):
            if dp[i] == dp[idx] - 1 and nums[i] < nums[idx]:
                trace.append(i)
                idx = i
        for i in reversed(trace):
            print(nums[i])
        return max(dp)
        
            