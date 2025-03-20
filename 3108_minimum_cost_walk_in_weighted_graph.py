class Solution:
    def minimumCost(self, n: int, edges: list[list[int]], query: list[list[int]]) -> list[int]:
        parents = [i for i in range(n)]
        rank = [1] * n
        value = [-1] * n
        for edge in edges:
            v1, v2, val = edge
            while parents[v1] != parents[parents[v1]]:
                parents[v1] = parents[parents[v1]]
            while parents[v2] != parents[parents[v2]]:
                parents[v2] = parents[parents[v2]]
            val1, val2, = value[parents[v2]], value[parents[v1]]
            if parents[v1] != parents[v2]:
                if rank[parents[v1]] >= rank[parents[v2]]:
                    rank[parents[v1]] += rank[parents[v2]]
                    parents[parents[v2]] = parents[v1]
                else:
                    rank[parents[v2]] += rank[parents[v1]]
                    parents[parents[v1]] = parents[v2]
            value[parents[v2]] = value[parents[v1]
                                       ] = val1 & val2 & val

        res = [-1] * len(query)
        for i, q in enumerate(query):
            v1, v2 = q
            while parents[v1] != parents[parents[v1]]:
                parents[v1] = parents[parents[v1]]
            while parents[v2] != parents[parents[v2]]:
                parents[v2] = parents[parents[v2]]
            if parents[v1] != parents[v2]:
                continue
            res[i] = value[parents[v1]]
        return res


n = 4
edges = [[2, 1, 5], [0, 3, 15], [3, 2, 7]]
query = [[0, 3], [3, 0], [2, 3]]
output = [5, 5, 5]

obj = Solution()
res = obj.minimumCost(n, edges, query)
print(res)
print(output)
print(res == output)
