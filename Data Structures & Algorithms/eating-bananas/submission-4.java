class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        Arrays.sort(piles);
        int l = 1;
        int r = Arrays.stream(piles).max().getAsInt();
        int k = 0;
        int min_k = Integer.MAX_VALUE;
        while(l <= r){
            k = (l+r)/2;
            int time = 0;
            for(int i = 0; i < piles.length; ++i){
                time += Math.ceil((double)piles[i]/k);
            }
            if(time <= h){
                r = k -1;
                min_k = Math.min(min_k, k);
            }else{
                l = k+1;
            }

        }
        return min_k;
    }
}
