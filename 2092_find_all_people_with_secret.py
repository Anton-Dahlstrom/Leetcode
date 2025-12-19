from collections import defaultdict


class Solution:
    def findAllPeople(self, n: int, meetings: list[list[int]], firstPerson: int) -> list[int]:
        meetings.sort(key=lambda x: x[2])
        m = len(meetings)
        groups = []
        edges = []
        prevTime = meetings[0][2]
        for i in range(m):
            p1, p2, time = meetings[i]
            if time != prevTime:
                groups.append(edges)
                edges = []
                prevTime = time
            edges.append([p1, p2])
        groups.append(edges)
        hasSecret = {0, firstPerson}

        for time in groups:
            graph = defaultdict(set)
            start = set()
            for p1, p2 in time:
                graph[p1].add(p2)
                graph[p2].add(p1)
                if p1 in hasSecret:
                    start.add(p1)
                if p2 in hasSecret:
                    start.add(p2)
            # bfs with hasSecret as visited
            for person in start:
                arr = [person]
                while arr:
                    temp = []
                    for p in arr:
                        for nextp in graph[p]:
                            if nextp not in hasSecret:
                                hasSecret.add(nextp)
                                temp.append(nextp)
                    arr = temp

        return list(hasSecret)


n = 6
meetings = [[1, 2, 5], [2, 3, 8], [1, 5, 10]]
firstPerson = 1
output = [0, 1, 2, 3, 5]

obj = Solution()
res = obj.findAllPeople(n, meetings, firstPerson)
print(res)
print(output)
print(res == output)
