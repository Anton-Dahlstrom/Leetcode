class Solution:
    def processQueries(self, c: int, connections: list[list[int]], queries: list[list[int]]) -> list[int]:
        parents = [i for i in range(c+1)]

        def updateParent(node, parents):
            p = parents[node]
            while parents[p] != p:
                p = parents[p]
            parents[node] = p

        for v, u in connections:
            updateParent(v, parents)
            updateParent(u, parents)
            final = min(parents[v], parents[u])
            parents[parents[v]] = final
            parents[parents[u]] = final
            parents[v] = final
            parents[u] = final

        groups = {}  # parents : list
        for i in range(1, c+1):
            updateParent(i, parents)
            if parents[i] not in groups:
                groups[parents[i]] = [i]
            else:
                groups[parents[i]].append(i)
        for key in groups:
            groups[key].sort(reverse=True)

        res = []
        dead = set()
        for query, node in queries:
            if query == 1:
                if node in dead:
                    updateParent(node, parents)
                    livenode = -1
                    while groups[parents[node]]:
                        if groups[parents[node]][-1] in dead:
                            groups[parents[node]].pop()
                        else:
                            livenode = groups[parents[node]][-1]
                            break
                    res.append(livenode)
                else:
                    res.append(node)
            elif query == 2:
                dead.add(node)
        return res


c = 5
connections = [[1, 2], [2, 3], [3, 4], [4, 5]]
queries = [[1, 3], [2, 1], [1, 1], [2, 2], [1, 2]]
output = [3, 2, 3]

obj = Solution()
res = obj.processQueries(c, connections, queries)
print(res)
print(output)
print(res == output)
