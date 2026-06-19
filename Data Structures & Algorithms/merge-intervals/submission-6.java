class Solution {
    public int[][] merge(int[][] intervals) {
        List<int[]> result = new ArrayList<>();
        Arrays.sort(intervals, (x,y) -> Integer.compare(x[0],y[0]));
        int[] current = intervals[0];

        for(int i = 1; i < intervals.length; ++i){
            int[] next = intervals[i];
            if(current[1] >= next[0]){
                current[1] = Math.max(next[1], current[1]);
            }else{
                result.add(current);
                current = next;
            }
        }
        result.add(current);
        return result.toArray(new int[result.size()][2]);
    }
}
