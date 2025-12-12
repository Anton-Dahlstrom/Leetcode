from collections import deque


class Solution:
    def countMentions(self, numberOfUsers: int, events: list[list[str]]) -> list[int]:
        n = numberOfUsers
        online = [1]*n
        mentions = [0]*n
        events.sort(key=lambda x: x[0], reverse=True)
        events.sort(key=lambda x: int(x[1]))
        offline = deque()
        for type, time, users in events:
            time = int(time)
            while offline and offline[-1][0] <= time:
                online[offline[-1][1]] = 1
                offline.pop()
            if users == "HERE":
                users = [int(i) for i in range(n) if online[i]]
            elif users == "ALL":
                users = [i for i in range(n)]
            else:
                users = users.split(" ")
                temp = []
                for user in users:
                    if user[:2] == "id":
                        user = user[2:]
                    temp.append(int(user))
                users = temp

            if type == "OFFLINE":
                for user in users:
                    offline.appendleft((time+60, user))
                    online[user] = 0

            elif type == "MESSAGE":
                for user in users:
                    mentions[user] += 1

        return mentions


numberOfUsers = 3
events = [["MESSAGE", "2", "HERE"], ["OFFLINE", "2", "1"],
          ["OFFLINE", "1", "0"], ["MESSAGE", "61", "HERE"]]
output = [1, 0, 2]

obj = Solution()
res = obj.countMentions(numberOfUsers, events)
print(res)
print(output)
print(res == output)
