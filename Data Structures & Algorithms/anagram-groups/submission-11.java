class Solution {
    public String hash(String str){
        int[] arr = new int[26];
        for(int i = 0; i < str.length(); ++i){
            arr[str.charAt(i) - 97] += 1;
        }
        return Arrays.stream(arr)
            .mapToObj(String::valueOf)
            .collect(Collectors.joining("#"));
    }
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> map = new HashMap<>();
        for(String str : strs){
            String key = hash(str);
            List<String> anagrams = map.getOrDefault(key, new ArrayList<String>());
            anagrams.add(str);
            map.put(key, anagrams);
        }
        return map.entrySet().stream()
                    .flatMap(x -> Stream.of(x.getValue()))
                    .toList();
    }
}
