//Take the current index j
// if total + arr[j] = k, count += 1. Increment j
// if total + arr[j] < k them expand to right and check
// if total + arr[j] > k, shrink from left till runningSum <= k
class Solution {
    public int subarraySum(int[] nums, int k) {
        int count = 0;
        int runningSum = 0;
        Map<Integer, Integer> freq = new HashMap<>();
        freq.put(0, 1);
        for(int i = 0; i < nums.length; ++i){
            runningSum += nums[i];
            count += freq.getOrDefault(runningSum - k, 0);
            freq.put(runningSum, freq.getOrDefault(runningSum, 0) + 1);
        }

        return count;
    }
}