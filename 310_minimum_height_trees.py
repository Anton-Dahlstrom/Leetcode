from collections import defaultdict


class Solution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        if not edges:
            return [i for i in range(n)]
        graph = defaultdict(set)
        degree = [0]*n
        for edge in edges:
            parent, child = edge
            graph[child].add(parent)
            graph[parent].add(child)
            degree[parent] += 1
            degree[child] += 1

        arr = []
        visited = set()
        for i in range(n):
            if degree[i] == 1:
                arr.append(i)
                visited.add(i)
        temp = arr
        while arr:
            temp = []
            for node in arr:
                for parent in graph[node]:
                    if parent not in visited:
                        degree[parent] -= 1
                        graph[parent].remove(node)
                        if degree[parent] == 1:
                            temp.append(parent)
                            visited.add(parent)
            if not temp:
                return arr
            arr = temp


n = 6
edges = [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]
output = [3, 4]

n = 7
edges = [[0, 1], [1, 2], [1, 3], [2, 4], [3, 5], [4, 6]]
output = [1, 2]

obj = Solution()
res = obj.findMinHeightTrees(n, edges)
print(res)
print(output)
print(res == output)
