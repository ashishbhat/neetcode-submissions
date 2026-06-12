class Solution {
    public String mergeAlternately(String word1, String word2) {
        int left = 0;
        int right = 0;
        StringBuilder str = new StringBuilder("");

        boolean l = true;
        while(left < word1.length() && right < word2.length()){
            if(l){
                str.append(word1.charAt(left));
                left++;
            }else {
                str.append(word2.charAt(right));
                right++;
            }
            l = !l;
        }
        if(left < word1.length()){
            str.append(word1.substring(left, word1.length()));
        }else if(right < word2.length()){
            str.append(word2.substring(right, word2.length()));
        }
        return str.toString();
    }
}