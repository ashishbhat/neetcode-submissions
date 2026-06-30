class Solution {
    public int[][] merge(int[][] intervals) {
        Arrays.sort(intervals, (x,y) -> Integer.compare(x[0], y[0]));
        List<int[]> result = new ArrayList<>();

        int[] currentInterval = intervals[0];
        for(int i = 0; i < intervals.length; ++i){
            int[] nextInterval = intervals[i];
            if(nextInterval[0] <= currentInterval[1]){
                // extend the current interval
                currentInterval[1] = Math.max(currentInterval[1], nextInterval[1]);
                continue;
            }
            result.add(currentInterval);
            currentInterval = nextInterval;
        }
        result.add(currentInterval);
        return result.toArray(new int[result.size()][]);
        
    }
}
