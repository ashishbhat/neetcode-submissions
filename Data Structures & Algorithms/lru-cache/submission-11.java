class LRUCache {
    class Entry{
        Entry next;
        Entry prev;
        int key;
        int val;

        public Entry(int key, int val){
            this.next = null;
            this.prev = null;
            this.val = val;
            this.key = key;
        }
    }

    private Entry head;
    private Entry tail;
    private final Map<Integer, Entry> entryMap;
    private int capacity;

    public LRUCache(int capacity) {
        this.capacity = capacity;
        this.entryMap = new HashMap<Integer, Entry>(capacity);
        this.head = null;
        this.tail = null;
    }
    
    public int get(int key) {
        if(!entryMap.containsKey(key)){
            return -1;
        }
        Entry e = entryMap.get(key);
        removeEntry(e);
        addToTail(e);
        return e.val;
    }
    
    public void put(int key, int value) {
        if(entryMap.containsKey(key)){
            Entry e = entryMap.get(key);
            removeEntry(e);
            e.val = value;
            addToTail(e);
        }else{
            if(entryMap.size() == capacity){
                removeEntry(head);
            }
            Entry e = new Entry(key, value);
            addToTail(e);
        }
    }

    private void removeEntry(Entry e){
        if(head == tail){
            head = null;
            tail = null;
        }else if(e == head){
            head = head.next;
            head.prev.next = null;
            head.prev = null;
        }else if(e == tail){
            tail = tail.prev;
            tail.next.prev = null;
            tail.next = null;
        }else{
            e.prev.next = e.next;
            e.next.prev = e.prev;
            e.next = null;
            e.prev = null;
        }
        entryMap.remove(e.key);
    }

    private void addToTail(Entry e){
        if(head == null && tail == null){
            head = e;
            tail = e;
        }else{
            tail.next = e;
            e.prev = tail;
            tail = e;
        }
        entryMap.put(e.key, e);
    }
}
