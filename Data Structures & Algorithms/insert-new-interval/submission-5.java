class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        List<int[]> result = new ArrayList<>();
        if(intervals.length == 0){
            return new int[][]{newInterval};
        }
        int[] currentInterval = intervals[0];
        if(currentInterval[0] > newInterval[0]){
            currentInterval = newInterval;
        }
        for(int i = 0; i < intervals.length; ++i){
            int[] nextInterval = intervals[i];
            if( newInterval[0] >= currentInterval[0] && 
                newInterval[0] <= currentInterval[1]){
                currentInterval[1] = Math.max(currentInterval[1], newInterval[1]);
            }else if(newInterval[0] > currentInterval[1] && newInterval[0] < nextInterval[0]){
                result.add(currentInterval);
                currentInterval = newInterval;
            }
            if(nextInterval[0] <= currentInterval[1]){
                // extend the current interval
                currentInterval[1] = Math.max(currentInterval[1], nextInterval[1]);
                continue;
            }
            result.add(currentInterval);
            currentInterval = nextInterval;
        }
        result.add(currentInterval);
        if(newInterval[0] > intervals[intervals.length - 1][1]){
            result.add(newInterval);
        }
        return result.toArray(new int[result.size()][]);
    }
}