class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        edgehmap = {}
        for edge in edges:
            if edge[1] in edgehmap:
                edge[1].append(edge[0])
            else:
                edgehmap.setdefault(edge[0], []).append(edge[1])

        def dfs(val):
            res = False
            if val not in visited:
                visited.add(val)
            if val in edgehmap:
                for v in edgehmap[val]:
                    if dfs(v):
                        res = True
            return res

        visited = set()
        for node in edgehmap:
            if node not in visited:
                dfs(node)
        print(edgehmap)
        pass


n = 6
edges = [[0, 1], [1, 2], [2, 3], [4, 5]]
output = 2

obj = Solution()
res = obj.countComponents(n, edges)
print(res)
print(res == output)
