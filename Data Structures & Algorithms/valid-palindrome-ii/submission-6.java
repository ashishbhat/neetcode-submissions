class Solution {
    public boolean isPalindrome(String s, int left, int right){
        while(left < right){
            if(s.charAt(right) != s.charAt(left)){
                return false;
            }
            ++left;
            --right;
        }
        return true;
    }
    public boolean validPalindrome(String s) {
        int i = 0;
        int j = s.length() - 1;

        while( i < j){
            if(s.charAt(i) != s.charAt(j)){
                return isPalindrome(s, i, j-1) || isPalindrome(s, i+1, j);
            } 
            ++i;
            --j;
        }
        return true;
    }
    
}