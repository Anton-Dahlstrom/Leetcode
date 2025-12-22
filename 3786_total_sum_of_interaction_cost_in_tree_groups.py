from collections import defaultdict


class Solution:
    def interactionCosts(self, n: int, edges: list[list[int]], group: list[int]) -> int:
        graph = [[]for _ in range(n)]
        self.group = group
        self.res = 0
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = {0}

        def dfs(cur):
            groups = defaultdict(list)  # group: [totaldepth, nodeCount]
            group = self.group[cur]
            groups[group] = [0, 1]
            for node in graph[cur]:
                if node not in visited:
                    visited.add(node)
                    newGroups = dfs(node)
                    for newGroup in newGroups:
                        if newGroup in groups:
                            self.res += (newGroups[newGroup][0] * groups[newGroup]
                                         [1]) + newGroups[newGroup][1] * groups[newGroup][0]
                            groups[newGroup][0] += newGroups[newGroup][0]
                            groups[newGroup][1] += newGroups[newGroup][1]
                        else:
                            groups[newGroup] = newGroups[newGroup].copy()
            for group in groups:
                groups[group][0] += groups[group][1]
            return groups

        dfs(0)
        return self.res


n = 3
edges = [[0, 1], [1, 2]]
group = [1, 1, 1]
output = 4

obj = Solution()
res = obj.interactionCosts(n, edges, group)
print(res)
print(output)
print(res == output)
