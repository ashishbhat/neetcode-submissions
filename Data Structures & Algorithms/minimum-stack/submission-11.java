class MinStack {
    private Deque<int[]> stack;

    public MinStack() {
        stack = new ArrayDeque<>();
    }
    
    public void push(int val) {
        int min = 0;
        if(stack.isEmpty()){
            min = val;
        }else{
            min = Math.min(val, stack.peekLast()[1]);
        }
        stack.offerLast(new int[]{val, min});
    }
    
    public void pop() {
        stack.pollLast();
    }
    
    public int top() {
        return stack.peekLast()[0];
    }
    
    public int getMin() {
        return stack.peekLast()[1];
    }
}
