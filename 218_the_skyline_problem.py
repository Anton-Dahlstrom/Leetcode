import heapq


class Solution:
    def getSkyline(self, buildings: list[list[int]]) -> list[list[int]]:
        events = [[0, 0, 0], [float("inf"), 0, 1]]
        for b in buildings:
            events.append([b[0], -b[2], 0])
            events.append([b[1], b[2], 1])
        events.sort()
        removing = {}
        heap = []
        prevheight = 0
        res = []
        lastend = 0
        for e in events:
            i, height, end = e
            # Start of building = add height
            if not end:
                heapq.heappush(heap, height)
            else:
                if -height == heap[0]:
                    heapq.heappop(heap)
                    while heap and heap[0] in removing:
                        removing[heap[0]] -= 1
                        if removing[heap[0]] == 0:
                            removing.pop(heap[0])
                        heapq.heappop(heap)
                else:
                    removing.setdefault(-height, 0)
                    removing[-height] += 1
                if i < float("inf"):
                    lastend = i
            if heap and heap[0] != prevheight:
                res.append([i, heap[0] * -1])
                prevheight = heap[0]
        res[-1][0] = lastend
        return res


buildings = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]
output = [[2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0]]


obj = Solution()
res = obj.getSkyline(buildings)
print(res)
print(output)
print(res == output)
