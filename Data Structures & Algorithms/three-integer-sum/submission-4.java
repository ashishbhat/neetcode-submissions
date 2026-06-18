class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        Set<List<Integer>> result = new HashSet<>();
        for(int i = 0; i < nums.length - 2; ++i){
            int p1 = i + 1;
            int p2 = nums.length - 1;
            int required = -nums[i];
            while(p1 < p2){
                if ((nums[p1] + nums[p2]) < required){
                    ++p1;
                }else if((nums[p1] + nums[p2]) > required){
                    --p2;
                }else{
                    result.add(List.of(nums[i], nums[p1], nums[p2]));
                    ++p1;
                    --p2;
                }
            }
        }
        return new ArrayList<>(result);
    }
}
