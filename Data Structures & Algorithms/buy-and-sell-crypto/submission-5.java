class Solution {
    public int maxProfit(int[] prices) {
        int lowestPrice = Integer.MAX_VALUE;;
        int maxProfit = 0;
        for(int i = 0; i < prices.length; ++i){
            lowestPrice = Math.min(lowestPrice, prices[i]);
            maxProfit = Math.max(maxProfit, prices[i] - lowestPrice);
        }
        return maxProfit;
    }
}
