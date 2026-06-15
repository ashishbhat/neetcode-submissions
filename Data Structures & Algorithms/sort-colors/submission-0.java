class Solution {
    private void swap(int[] arr, int i, int j){
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    public void sortColors(int[] nums) {
        int z = 0; // position of next 0
        int t = nums.length - 1; // position of next 2
        int j = 0; // scan index

        while(j <= t){
            if(nums[j] == 0){
                swap(nums, z, j);
                ++z;
                ++j;
            }else if(nums[j] == 2){
                swap(nums, t, j);
                --t;
            }else{
                ++j;
            }
        }
    }
}