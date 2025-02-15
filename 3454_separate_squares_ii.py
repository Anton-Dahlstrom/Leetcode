import heapq


class Solution:
    def separateSquares(self, squares: list[list[int]]) -> float:

        events = []
        for i in range(len(squares)):
            x, y, side = squares[i]
            heapq.heappush(events, (y, side))
            heapq.heappush(events, (y+side, -1*side))

        eventscopy = events.copy()

        cursides = [0]
        sideremove = []
        previ = events[0][0] - 1
        totalsize = 0
        while events:
            i = events[0][0]
            while events and events[0][0] == i:
                j, side = heapq.heappop(events)
                if side >= 0:
                    heapq.heappush(cursides, side*-1)
                else:
                    heapq.heappush(sideremove, side)
            while sideremove and sideremove[0] == cursides[0]:
                heapq.heappop(sideremove)
                heapq.heappop(cursides)
            curside = cursides[0]*-1
            totalsize += curside * abs((i - previ))
            previ = i

        events = eventscopy
        target = round(totalsize / 2, 7)
        cursides = [0]
        sideremove = []
        cursize = 0
        previ = events[0][0]
        l = 0
        r = 0

        while events:
            i = events[0][0]
            while events and events[0][0] == i:
                j, side = heapq.heappop(events)
                if side >= 0:
                    heapq.heappush(cursides, side*-1)
                else:
                    heapq.heappush(sideremove, side)
            while sideremove and sideremove[0] == cursides[0]:
                heapq.heappop(sideremove)
                heapq.heappop(cursides)

            print("I", previ, i, curside, cursize, curside * (i-previ))
            if cursize + round((curside * (i - previ)), 7) == target:
                print('hi', previ, i, curside, cursize, target)
                return i
            if cursize + curside * (i - previ) > target:
                l = previ
                r = i
                break
            curside = cursides[0]*-1
            cursize += curside * (i - previ)
            previ = i

        lstart = l
        while round(l, 7) != round(r, 7):
            mid = l + ((r-l)/2)
            val = round(curside * (mid - lstart), 7)
            if val > target:
                if round(r-mid, 7) == 0:
                    return mid
                r = mid
            elif val < target:
                if round(l-mid, 7) == 0:
                    return mid
                l = mid
            else:
                return mid

        return l


squares = [[0, 0, 2], [1, 1, 1]]
output = 1.00000

squares = [[0, 0, 1], [2, 2, 1]]
output = 1.00000

obj = Solution()
res = obj.separateSquares(squares)
print(res)
print(output)
print(res == output)
