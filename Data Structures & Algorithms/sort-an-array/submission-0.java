class Solution {
    public int[] sortArray(int[] nums) {
        Queue<Integer> heap = new PriorityQueue<>();
        for(int i : nums){
            heap.offer(Integer.valueOf(i));
        }
        //int[] result = new int[nums.length];
        int i = 0;
        while(!heap.isEmpty()){
            nums[i++] = heap.poll();
        }
        return nums;
    }
}