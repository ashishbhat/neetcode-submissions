class TimeMap {
    private final Map<String,TreeMap<Integer, String>> store;


    public TimeMap() {
        store = new HashMap<String,TreeMap<Integer, String>>();
    }
    
    public void set(String key, String value, int timestamp) {
        TreeMap<Integer, String> timeMap = store.getOrDefault(key, null);
        if(timeMap == null){
            timeMap = new TreeMap<>();
        }
        timeMap.put(timestamp, value);
        store.put(key, timeMap);
    }
    
    public String get(String key, int timestamp) {
        TreeMap<Integer, String> timeMap = store.getOrDefault(key, null);
        String val = "";
        if(timeMap != null){
            Map.Entry<Integer, String> floor = timeMap.floorEntry(timestamp);
            if(floor != null){
                val = floor.getValue();
            }
        }
        return val;
    }
}
