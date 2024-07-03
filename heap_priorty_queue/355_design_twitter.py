from typing import List
import heapq


class Twitter:

    def __init__(self):
        self.time = 0
        self.following = {}  # Contains set
        self.tweets = {}  # Contains array with

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time -= 1
        self.tweets.setdefault(userId, []).append([self.time, tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        following = self.following.get(userId)
        feed = []
        if userId in self.following:
            following = self.following[userId]
            for user in following:
                if user in self.tweets:
                    for tweet in self.tweets[user]:
                        heapq.heappush(feed, tweet)
        if userId in self.tweets:
            for tweet in self.tweets[userId]:
                heapq.heappush(feed, tweet)
        return [heapq.heappop(feed)[1] for tweet in range(min(len(feed), 10))]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following.setdefault(followerId, set()).add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following:
            self.following[followerId].remove(followeeId)
