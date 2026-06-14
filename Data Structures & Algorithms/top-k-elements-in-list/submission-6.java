class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> freqMap = new HashMap<>();
        for(int i : nums){
            freqMap.put(i, freqMap.getOrDefault(i,0) + 1);
        }
        Comparator<int[]> comparator = (x, y) -> Integer.compare(x[1],y[1]);
        Queue<int[]> heap = new PriorityQueue<>(comparator);
        for(Map.Entry<Integer, Integer> m : freqMap.entrySet()){
            heap.offer(new int[]{m.getKey(), m.getValue()});
            if(heap.size() > k){
                heap.poll();
            }
        }
        return heap.stream()
                    .mapToInt(x -> x[0])
                    .toArray();

    }
}
