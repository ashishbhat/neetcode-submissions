class Solution {
    public int coinChangeHelper(int[] coins, int amount) {
        int INF = 1000000;
        int[]dp = new int[amount+1];
        Arrays.fill(dp, INF);
        dp[0] = 0;
        for(int target = 1; target <= amount ; ++target){
            for(int coin : coins){
                if(coin <= target){
                    dp[target] = Math.min(dp[target], 1 + dp[target - coin]);
                }
            }
        }
        return dp[amount];
    }
    public int coinChange(int[] coins, int amount) {
            int result = coinChangeHelper(coins, amount);
            return result >= 1000000 ? -1 : result;
    }
}
