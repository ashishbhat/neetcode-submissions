class Solution {
    public int connectSticks(int[] sticks) {
        Queue<Integer> heap = new PriorityQueue<>();
        for(int stick : sticks){
            heap.offer(stick);
        }
        int totalCost = 0;
        while(heap.size() > 1){
            int first = heap.poll();
            int second = heap.poll();
            int cost = first + second;
            totalCost += cost;
            heap.offer(cost);
        }
        return totalCost;
    }
}
