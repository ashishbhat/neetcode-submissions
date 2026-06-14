class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> freqMap = new HashMap<>();
        for(int i : nums){
            freqMap.put(i, freqMap.getOrDefault(i,0) + 1);
        }
        Comparator<Integer[]> comparator = (x, y) -> x[1]-y[1];
        Queue<Integer[]> heap = new PriorityQueue<>(comparator);
        for(Map.Entry<Integer, Integer> m : freqMap.entrySet()){
            heap.offer(new Integer[]{m.getKey(), m.getValue()});
            if(heap.size() > k){
                heap.poll();
            }
        }
        return heap.stream()
                    .mapToInt(x -> x[0])
                    .toArray();

    }
}
