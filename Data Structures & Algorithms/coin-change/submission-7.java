class Solution {
    public int coinChangeHelper(int[] coins, int amount, int[] dp) {
        if(dp[amount] != -1){
            return dp[amount];
        }
        int minCoins = Integer.MAX_VALUE;
        for(int coin : coins){
            if(coin <= amount){
                int res = coinChangeHelper(coins, amount - coin, dp);
                if(res == Integer.MAX_VALUE){
                    res = Integer.MAX_VALUE;
                }else{
                    res += 1;
                }
                minCoins = Math.min(minCoins, res);
            }
        }

        dp[amount] = minCoins;
        return minCoins;
    }
    public int coinChange(int[] coins, int amount) {
            int[]dp = new int[amount+1];
            Arrays.fill(dp, -1);
            dp[0] = 0;
            int result = coinChangeHelper(coins, amount, dp);
            return result == Integer.MAX_VALUE ? -1 : result;
    }
}
