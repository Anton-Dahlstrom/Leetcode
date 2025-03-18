class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        target = len(graph)-1
        path = [0]
        res = []

        def dfs():
            cur = path[-1]
            if cur == target:
                res.append(path.copy())
            for node in graph[cur]:
                path.append(node)
                dfs()
                path.pop()
        dfs()
        return res


graph = [[4, 3, 1], [3, 2, 4], [3], [4], []]
output = [[0, 4], [0, 3, 4], [0, 1, 3, 4], [0, 1, 2, 3, 4], [0, 1, 4]]

obj = Solution()
res = obj.allPathsSourceTarget(graph)
print(res)
print(output)
print(res == output)
