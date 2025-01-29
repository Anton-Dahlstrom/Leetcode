from collections import defaultdict


class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        graph = defaultdict(set)

        def dfs(cur, target):
            if cur in visited:
                return False

            visited.add(cur)
            if target in graph[cur]:
                return True

            for edge in graph[cur]:
                if dfs(edge, target):
                    return True
            return False
        for edge in edges:
            parent, child = edge
            visited = set()
            if dfs(parent, child):
                return edge
            graph[parent].add(child)
            graph[child].add(parent)


edges = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
output = [1, 4]

obj = Solution()
res = obj.findRedundantConnection(edges)
print(res)
print(output)
print(res == output)
