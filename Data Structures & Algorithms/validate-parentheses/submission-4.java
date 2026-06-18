class Solution {
    public boolean isValid(String s) {
        java.util.Deque<Character> stack= new java.util.ArrayDeque<>();
        int n = s.length();
        Map<Character, Character> map = new HashMap<>();
        map.put(')','(');
        map.put(']','[');
        map.put('}','{');

        for(int i = 0; i < n; ++i){
            char ch = s.charAt(i);
            if(map.containsKey(ch)){
                if(stack.peekLast() == map.get(ch)){
                    stack.pollLast();
                }else{
                    return false;
                }
            }else{
                stack.offerLast(ch);
        }
    }
    if(stack.isEmpty()) return true;
    return false;
}
}