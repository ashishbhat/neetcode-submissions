class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> s = new HashSet<>();
        for(int i : nums){
            s.add(i);
        }
        int answer = 0;

        for(int i = 0; i < nums.length; ++i){
            if(s.contains(nums[i] - 1)){
                continue;
            }
            int temp = 1;
            int next = nums[i] + 1;
            while(s.contains(next)){
                ++temp;
                ++next;
                answer = Math.max(answer, temp);
            }
            answer = Math.max(temp, answer);
        }
        return answer;
    }
}
