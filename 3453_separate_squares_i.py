import heapq


class Solution:
    def separateSquares(self, squares: list[list[int]]) -> float:
        totalsize = 0
        events = []
        for i in range(len(squares)):
            x, y, side = squares[i]
            heapq.heappush(events, (y, side))
            heapq.heappush(events, (y+side, -1*side))
            totalsize += side**2

        target = totalsize/2
        cursize = 0
        curside = 0
        previ = events[0][0] - 1
        l = 0
        r = 0

        while events:
            i, side = heapq.heappop(events)
            while events and events[0][0] == i:
                j, jside = heapq.heappop(events)
                side += jside
            if cursize + curside * (i - previ) == target:
                return i
            if cursize + curside * (i - previ) > target:
                l = previ
                r = i
                break
            cursize += curside * (i - previ)
            curside += side
            previ = i
            # print(cursize)

        target -= cursize

        # print(l, r, curside, cursize, target)
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
output = 1.16667

squares = [[0, 0, 1], [2, 2, 1]]
output = 1.00000

squares = [[7, 16, 4], [3, 13, 4]]
output = 16.50000
squares = [[522261215, 954313664, 461744743], [628661372, 718610752, 21844764], [619734768, 941310679, 91724451], [352367502, 656774918, 591943726], [860247066, 905800565, 853111524], [
    817098516, 868361139, 817623995], [580894327, 654069233, 691552059], [182377086, 256660052, 911357], [151104008, 908768329, 890809906], [983970552, 992192635, 462847045]]

obj = Solution()
res = obj.separateSquares(squares)
print(res)
print(output)
print(res == output)
