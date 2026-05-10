class Solution {
    public boolean checkInclusion(String s1, String s2) {
        if(s2.length() < s1.length()) return false;
        int[] targetFreq = new int[26];   
        int[] currentFreq = new int[26];

        for(int i = 0; i < s1.length(); ++i){
            targetFreq[s1.charAt(i) - 'a']++;
            currentFreq[s2.charAt(i) - 'a']++;
        }        
        if(Arrays.equals(targetFreq, currentFreq)) return true;

        int left = 0;
        for(int right = s1.length(); right < s2.length(); ++right){
            currentFreq[s2.charAt(left) - 'a']--;
            currentFreq[s2.charAt(right) - 'a']++;
            if(Arrays.equals(targetFreq, currentFreq)) return true;
            left += 1;
        }
        return false;
     
    }
}
