class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: list[list[int]]) -> list[int]:
        res = []
        edges = {}
        # Create initial roads
        for i in range(n-1):
            connections = set()
            connections.add(i+1)
            edges[i] = connections

        for road in queries:
            # Add new roads
            leftCity, rightCity = road
            edges[leftCity].add(rightCity)

            # Bfs search that runs until the last city (n-1) is found
            cur = {0}
            count = 0
            found = False
            while not found:
                temp = set()
                count += 1
                for city in cur:
                    for edge in edges[city]:
                        if edge == n-1:
                            res.append(count)
                            found = True
                            break
                        temp.add(edge)
                    if found:
                        break
                cur = temp

        return res


n = 5
queries = [[2, 4], [0, 2], [0, 4]]
output = [3, 2, 1]

obj = Solution()
res = obj.shortestDistanceAfterQueries(n, queries)
print(res)
print(output)
print(res == output)
