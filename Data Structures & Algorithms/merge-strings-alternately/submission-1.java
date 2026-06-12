class Solution {
    public String mergeAlternately(String word1, String word2) {
        int left = 0;
        int right = 0;
        String str = "";

        boolean l = true;
        while(left < word1.length() && right < word2.length()){
            if(l){
                str = str + word1.charAt(left);
                left++;
            }else {
                str = str + word2.charAt(right);
                right++;
            }
            l = !l;
        }
        if(left < word1.length()){
            str = str + word1.substring(left, word1.length());
        }else if(right < word2.length()){
            str = str + word2.substring(right, word2.length());
        }
        return str;
    }
}