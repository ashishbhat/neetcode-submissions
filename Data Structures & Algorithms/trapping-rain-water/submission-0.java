class Solution {
    public int trap(int[] height) {
        int n = height.length;
        int[]   left = new int[n];
        int[]   right =     new int[n];
        int[]   water = new int[n];

        int left_max  = 0;
        int right_max = 0;

        for(int i = 0; i < n; ++i){
            left[i] = left_max;
            left_max = Math.max(left_max, height[i]);
        }

        for(int i = n-1; i >= 0; --i){
            right[i] = right_max;
            right_max = Math.max(right_max, height[i]);
        }
        for(int i = 0; i < n; ++i){
            if(height[i] < left[i] && height[i] < right[i]){
                water[i] = Math.min(left[i],right[i]) - height[i];
            }
        }
        return Arrays.stream(water).sum();
    }
}
