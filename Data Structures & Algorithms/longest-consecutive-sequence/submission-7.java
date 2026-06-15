class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> s = new HashSet<>();
        for(int i : nums){
            s.add(i);
        }
        int answer = 0;

        for(int i = 0; i < nums.length; ++i){
            int temp = 1;
            answer = Math.max(answer, temp);
            int next = nums[i] + 1;
            while(s.contains(next)){
                ++next;
                temp += 1;
                answer = Math.max(answer, temp);
            }
        }
        return answer;
    }
}
