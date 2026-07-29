class Twitter {

    record Tweet(int count, int tweetId){}

    private Map<Integer, Set<Integer>> followees;
    private Map<Integer, List<Tweet>> tweets;
    private int counter = 0;

    public Twitter() {
        followees = new HashMap<Integer, Set<Integer>>();
        tweets = new HashMap<Integer, List<Tweet>>();
    }
    
    public void postTweet(int userId, int tweetId) {
        Tweet tweet = new Tweet(counter++, tweetId);
        tweets.computeIfAbsent(userId, k -> new ArrayList<Tweet>())
                .add(tweet);
    }
    
    public List<Integer> getNewsFeed(int userId) {
        Set<Integer> users = followees.getOrDefault(userId, new HashSet<Integer>());
        users.add(userId);
        List<Tweet> feed = new ArrayList<>();

        for(Integer user : users){
            feed.addAll(tweets.getOrDefault(user, Collections.emptyList()));
        }
        return feed.stream()
            .sorted(Comparator.comparing(Tweet::count).reversed())
            .limit(10)
            .map(tweet -> tweet.tweetId())
            .toList();

    }
    
    public void follow(int followerId, int followeeId) {
        followees.computeIfAbsent(followerId, k -> new HashSet<Integer>())
                .add(followeeId);
    }
    
    public void unfollow(int followerId, int followeeId) {
        followees.get(followerId).remove(followeeId);
    }
}
