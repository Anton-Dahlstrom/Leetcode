from collections import defaultdict


class Solution:
    def reachableNodes(self, n: int, edges: list[list[int]], restricted: list[int]) -> int:
        graph = defaultdict(set)
        for e in edges:
            left, right = e
            graph[left].add(right)
            graph[right].add(left)
        visited = set(restricted)
        visited.add(0)
        arr = [0]
        res = 1
        while arr:
            temp = []
            for node in arr:
                for edge in graph[node]:
                    if edge not in visited:
                        visited.add(edge)
                        res += 1
                        temp.append(edge)
            arr = temp
        return res


n = 7
edges = [[0, 1], [1, 2], [3, 1], [4, 0], [0, 5], [5, 6]]
restricted = [4, 5]
output = 4

obj = Solution()
res = obj.reachableNodes(n, edges, restricted)
print(res)
print(output)
print(res == output)
