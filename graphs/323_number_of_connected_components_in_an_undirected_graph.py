class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        if not edges:
            return n
        edgehmap = {}
        for edge in edges:
            edgehmap.setdefault(edge[0], []).append(edge[1])
            edgehmap.setdefault(edge[1], []).append(edge[0])

        def dfs(val):
            res = False
            if val not in visited:
                visited.add(val)
            if val in edgehmap:
                for v in edgehmap[val]:
                    if v not in visited:
                        if dfs(v):
                            res = True
            return res

        count = 0
        visited = set()
        for i in range(n):
            if i not in visited:
                if not dfs(i):
                    count += 1

        return count


n = 6
edges = [[0, 1], [1, 2], [2, 3], [4, 5]]
output = 2


obj = Solution()
res = obj.countComponents(n, edges)
print(res)
print(res == output)
