class Solution {
    private final Random random = new Random();

    public void quickSort(int[] arr, int l, int r){
        
        if( r - l <= 1){
            return;
        }
        int pivotIndex = l + random.nextInt(r - l);
        swap(arr, l, pivotIndex);
        int i = l+1;
        int j = l + 1;
        int pivot = arr[l];
        while(j < r){
            if(arr[j] <= pivot){
                swap(arr, i, j);
                ++i;
                ++j;
            }else{
                ++j;
            }
        }
        swap(arr, i-1, l);
        quickSort(arr, l, i-1);
        quickSort(arr, i, r);
    }
    private void swap(int[] arr, int i, int j){
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
    public int[] sortArray(int[] nums) {
        quickSort(nums, 0, nums.length);
        return nums;
    }
}