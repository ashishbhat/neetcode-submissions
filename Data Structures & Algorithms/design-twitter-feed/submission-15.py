class Twitter:

    def __init__(self):
        self.followees = defaultdict(set)
        self.tweets = defaultdict(list)
        self.counter = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.counter, tweetId))
        self.counter += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        target = []
        target.extend(self.followees[userId])
        target.append(userId)
        feed = []
        for uid in set(target):
            feed.extend(self.tweets[uid])
        feed.sort(reverse=True, key = lambda tweet : tweet[0])
        return [tweet for _, tweet in feed[0:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followees:
            self.followees[followerId].discard(followeeId)

