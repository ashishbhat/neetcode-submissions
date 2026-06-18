class Solution {
    public String minWindow(String s, String t) {
        Map<Character, Integer> target = new HashMap<>();
        Map<Character, Integer> window = new HashMap<>();
        if(t.length() > s.length()){
            return "";
        }
        for(int i = 0; i < t.length(); ++i){
            target.put(t.charAt(i), target.getOrDefault(t.charAt(i), 0) +1 );
        }
        int l = 0;
        int have = 0;
        int need = target.size();
        int best_l = 0;
        int best_r = s.length() - 1;
        boolean found = false;

        for(int r = 0; r < s.length(); ++r){
            window.put(s.charAt(r), window.getOrDefault(s.charAt(r), 0)+1);
            if(window.get(s.charAt(r)) == target.get(s.charAt(r))){
                ++have;
            }
            if(have == need){
                found = true;
                while(!target.containsKey(s.charAt(l)) || 
                      window.get(s.charAt(l)) > target.get(s.charAt(l))){
                        window.put(s.charAt(l), window.getOrDefault(s.charAt(l), 0) - 1);
                        ++l;
                }
                if(r - l < best_r - best_l){
                    best_r = r;
                    best_l = l;
                }
            }
        }
        return found ? s.substring(best_l, best_r + 1) : "";
    }
}
