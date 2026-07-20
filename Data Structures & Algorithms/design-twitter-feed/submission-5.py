class Twitter:
    
    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId)) 
        self.time -= 1       

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets = []

        for followed in self.following[userId]:
            if followed != userId:
                tweets += self.tweets[followed]
        tweets += self.tweets[userId]
        heapq.heapify(tweets)

        res = []

        i = 0
        while tweets and i < 10:
            res.append(heapq.heappop(tweets)[1])
            i += 1
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        print(self.following)
        self.following[followerId].remove(followeeId) if followeeId in self.following[followerId] else None