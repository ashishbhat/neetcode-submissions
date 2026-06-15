class Solution {
    public int majorityElement(int[] nums) {
        int max_count = 0;
        int answer  = 0;
        Map<Integer, Integer> freq = new HashMap<>();

        for(int i : nums){
            int count = freq.getOrDefault(i, 0) + 1;
            freq.put(i, count);
            if(count > max_count){
                max_count = count;
                answer = i;
            }
        }
        return answer;
        
    }
}