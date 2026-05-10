class Solution {
    public int carFleet(int target, int[] position, int[] speed) {
        float[] time = new float[position.length];
        List<Map.Entry<Integer,Integer>> cars = new ArrayList<>();
        for(int i = 0; i < position.length; ++i){
            Map.Entry<Integer, Integer> entry = new AbstractMap.SimpleImmutableEntry<>(position[i], speed[i]);
            cars.add(entry);
        }
        cars.sort(Comparator.comparing(Map.Entry<Integer, Integer>::getKey).reversed());
        for(int i = 0; i < position.length; ++i ){
            time[i] = ((float)target - cars.get(i).getKey())/cars.get(i).getValue();
            System.out.println(time[i]);
        }
        Deque<Float> carStack = new ArrayDeque<>();
        for(float t : time){
            if(carStack.isEmpty() || t > carStack.peekLast()){
                carStack.offerLast(t);
            }
        }
        return carStack.size();
    }
}
