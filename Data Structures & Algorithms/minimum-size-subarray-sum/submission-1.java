class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int minWindow = Integer.MAX_VALUE;
        int left = 0;
        int currentSum = 0;
        for(int right = 0;  right < nums.length; ++right){
            currentSum += nums[right];
            while(currentSum >= target && left <= right){
                minWindow = Math.min(minWindow, right - left + 1);
                currentSum -= nums[left];
                ++left;
            }
        }
        if(minWindow == Integer.MAX_VALUE){
            minWindow = 0;
        }
        return minWindow;

    }
}