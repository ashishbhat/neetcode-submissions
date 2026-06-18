class Solution {
    private int getHighestFrequency(int[] freq){
        int highest = 0;
        for(int i : freq){
            highest = Math.max(highest, i);
        }
        return highest;
    }
    public int characterReplacement(String s, int k) {
        int[] freq = new int[26];
        int left = 0;
        int max_window = 0;

        for(int right = 0; right < s.length(); ++right){
            freq[s.charAt(right) - 'A'] += 1;
            int window_size = right - left + 1;
            while(window_size - getHighestFrequency(freq) > k){
                freq[s.charAt(left) - 'A'] -= 1;
                left += 1;
                window_size = right - left + 1;
            }
            max_window = Math.max(max_window, right - left + 1);
        }
        return max_window;
    }
}