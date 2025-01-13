import heapq


class Solution:
    def smallestChair(self, times: list[list[int]], targetFriend: int) -> int:
        events = []
        seats = [i for i in range(len(times))]
        occupied = {}
        for i in range(len(times)):
            events.append((times[i][0], 1, i))
            events.append((times[i][1], 0, i))
        events.sort()
        for event in events:
            time, arriving, friend = event
            if arriving:
                seat = heapq.heappop(seats)
                if friend == targetFriend:
                    return seat
                occupied[friend] = seat
            else:
                seat = occupied.pop(friend)
                heapq.heappush(seats, seat)


times = [[7, 10], [6, 7], [1, 3], [2, 7], [4, 5]]
targetFriend = 0
output = output = 0

obj = Solution()
res = obj.smallestChair(times, targetFriend)
print(res)
print(output)
print(res == output)
