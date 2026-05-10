class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        int[] result = new int[nums.length - k + 1];
        PriorityQueue<int[]> topK = 
                        new PriorityQueue<>(k,(a,b) -> Integer.compare(b[1], a[1]));
        for(int i = 0; i < k; ++i){
            topK.offer(new int[]{i, nums[i]});
        }
        int j = -1;
        result[++j] = topK.peek()[1];
        for(int i = 1; i < nums.length - k + 1; ++i){
            topK.offer(new int[] {i + k - 1, nums[i + k -1]});
            while(topK.peek()[0] < i){
                topK.poll();
            }
            result[++j] = topK.peek()[1];
        }
        return result;

    }
}
