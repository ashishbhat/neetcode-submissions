class Solution {
    private int lcs(String text1, String text2, int l1, int l2, int[][] dp){
        if(l1 == text1.length() || l2 == text2.length()){
            return 0;
        }
        if(dp[l1][l2] != -1){
            return dp[l1][l2];
        }
        if(text1.charAt(l1) == text2.charAt(l2)){
            dp[l1][l2] = 1 + lcs(text1, text2, l1+1, l2+1, dp);
            return dp[l1][l2];
        }else{
            int option1 = lcs(text1, text2, l1+1, l2, dp);
            int option2 = lcs(text1, text2, l1, l2+1, dp);
            dp[l1][l2] = Math.max(option1, option2);
            return dp[l1][l2];
        }
    }
    public int longestCommonSubsequence(String text1, String text2) {
        int[][] dp = new int[text1.length()][text2.length()];
        for (int i = 0; i < text1.length(); i++) {
            Arrays.fill(dp[i], -1);
        }
        return lcs(text1, text2, 0, 0, dp);
    }
}
