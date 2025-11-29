class Solution:
    def maxKDivisibleComponents(self, n: int, edges: list[list[int]], values: list[int], k: int) -> int:
        graph = [[] for _ in range(n)]
        self.res = 0
        for n, v in edges:
            graph[n].append(v)
            graph[v].append(n)

        def dfs(cur, prev):
            val = values[cur] % k
            for node in graph[cur]:
                if node != prev:
                    val += dfs(node, cur)
            val %= k
            if not val:
                self.res += 1
            return val
        dfs(0, -1)
        return self.res


n = 5
edges = [[0, 2], [1, 2], [1, 3], [2, 4]]
values = [1, 8, 1, 4, 4]
k = 6
output = 2

obj = Solution()
res = obj.maxKDivisibleComponents(n, edges, values, k)
print(res)
print(output)
print(res == output)
