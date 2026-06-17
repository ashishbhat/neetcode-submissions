class Solution {
    public int lengthOfLongestSubstring(String s) {
        Map<Character, Integer> seen = new HashMap<>();
        int left = 0;
        int longest = 0;
        StringBuilder result = new StringBuilder("");

        for(int right = 0; right < s.length(); ++right){
            Character current = s.charAt(right);
            if(seen.containsKey(current) && seen.get(current) >= left){
                left = seen.get(current) + 1;
            }else{
                longest = Math.max(longest, right - left + 1);
                result.setLength(0);
                result.append(s.substring(left, right+1));
                System.out.println(result);
            }
            seen.put(current, right);
        }
        return longest;
    }
}
