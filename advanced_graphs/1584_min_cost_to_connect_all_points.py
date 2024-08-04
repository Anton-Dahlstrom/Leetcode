import heapq


class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        if len(points) < 2:
            return 0

        def calcDistance(p1, p2):
            return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

        heap = []
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                distance = calcDistance(points[i], points[j])
                heapq.heappush(heap, [distance, i, j])

        added = set()
        connections = []
        res = 0
        while len(added) < len(points) or len(connections) > 1:
            stop = False
            dist, p1, p2 = heapq.heappop(heap)
            # Neither has a connection
            if p1 not in added and p2 not in added:
                connections.append(set([p1, p2]))

            # Both have a connection
            elif p1 in added and p2 in added:
                for index1 in range(len(connections)):
                    conn1 = connections[index1]
                    # Points are connected so we continue
                    if p1 in conn1 and p2 in conn1:
                        stop = True
                        continue
                    # Points are not connected so we find their sets and connect them
                    if p1 in conn1 or p2 in conn1:
                        for index2 in range(index1+1, len(connections)):
                            conn2 = connections[index2]
                            if p1 in conn2 or p2 in conn2:
                                conn1.update(connections.pop(index2))
                                break
                        break
            if stop:
                continue

            # One has a connection
            elif p1 in added or p2 in added:
                for conn in connections:
                    if p1 in conn or p2 in conn:
                        conn.update({p1, p2})
            added.update({p1, p2})
            res += dist

        return res


points = [[2, -3], [-17, -8], [13, 8], [-17, -15]]
output = 53

obj = Solution()
res = obj.minCostConnectPoints(points)
print(res)
print(res == output)
