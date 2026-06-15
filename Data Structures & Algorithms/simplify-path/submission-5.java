class Solution {
    final private List<String> ignoreList = Arrays.asList(".", "");
    final private Deque<String> stack = new ArrayDeque<>();

    void processToken(String token){
        switch(token){
            case ".." -> stack.pollLast();
            case "/"  -> {
                    if(stack.peekLast().equals("/")){
                        stack.removeLast();
                    }
                }
            default -> stack.offerLast(token);
        }
    }

    public String simplifyPath(String path) {
        String[] tokens = path.split("\\/");
        for(String token : tokens){
            if(!ignoreList.contains(token)){
                processToken(token);
            }
        }
        return "/" + stack.stream().collect(Collectors.joining("/"));

    }
}