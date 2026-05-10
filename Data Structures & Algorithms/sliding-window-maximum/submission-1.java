class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        PriorityQueue<Integer> topK = new PriorityQueue<>(k);
        List<Integer> result = new ArrayList<>();
        for(int i = 0; i < k; ++i){
            topK.offer(-nums[i]);
        }
        result.add(-topK.peek());
        int left = 0;
        for(int i = k; i < nums.length; ++i){
            topK.remove(-nums[left]);
            topK.offer(-nums[i]);
            result.add(-topK.peek());
            left += 1;
        }
        return result.stream().mapToInt(Integer::intValue).toArray();


    }
}
