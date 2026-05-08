class MinStack {
    Deque<int[]> stack; 

    public MinStack() {
        stack = new ArrayDeque<>();
    }
    
    public void push(int val) {
        if(this.stack.isEmpty()){
            stack.offerLast(new int[]{val, val});
        }else{
            int min = Math.min(this.getMin(), val);
            stack.offerLast(new int[]{val, min});
        }

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
