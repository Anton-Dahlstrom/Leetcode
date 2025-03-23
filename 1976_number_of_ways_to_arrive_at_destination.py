import heapq


class Solution:
    def countPaths(self, n: int, roads: list[list[int]]) -> int:
        graph = [{} for _ in range(n)]

        for road in roads:
            v1, v2, time = road
            graph[v1][v2] = time
            graph[v2][v1] = time

        # The solution involves a mix of Dijkstra's algo and dynamic programming.
        # This is where we store all candidates for departure.
        heap = [(0, 0)]  # time, node
        # Keeps track of the best time we managed to reach a node.
        bestTime = [float("inf")]*n
        # How many times we reached a node at it's best time.
        count = [0]*n
        # Set base case for dp.
        count[0] = 1
        while heap:
            time, node = heapq.heappop(heap)

            # Ensures we only depart from a given node once.
            if bestTime[node] < time:
                continue
            bestTime[node] = -1

            if node == n-1:
                break

            for newnode in graph[node]:
                newtime = graph[node][newnode] + time
                if newtime > bestTime[newnode]:
                    continue
                # If the new time is the same as the best time we add all the times we visited the current node
                # to the amount of times we visit the next node.
                elif newtime == bestTime[newnode]:
                    count[newnode] += count[node]
                # If our time is better then we reset the count of how many times we reached the next node.
                else:
                    count[newnode] = count[node]
                    bestTime[newnode] = newtime
                heapq.heappush(heap, (newtime, newnode))

        # Return how many times we reached the last node
        return count[n-1] % (10**9 + 7)


n = 7
roads = [[0, 6, 7], [0, 1, 2], [1, 2, 3], [1, 3, 3], [6, 3, 3],
         [3, 5, 1], [6, 5, 1], [2, 5, 1], [0, 4, 5], [4, 6, 2]]
output = 4

obj = Solution()
res = obj.countPaths(n, roads)
print(res)
print(output)
print(res == output)
