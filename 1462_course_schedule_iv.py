from collections import defaultdict


class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: list[list[int]], queries: list[list[int]]) -> list[bool]:
        adj = defaultdict(list)

        for req in prerequisites:
            preq, course = req
            adj[preq].append(course)

        def dfs(node, target):
            if node == target:
                return True
            if node in visited:
                return False
            visited.add(node)
            for edge in adj[node]:
                if dfs(edge, target):
                    return True
            return False

        res = []
        for query in queries:
            visited = set()
            preq, course = query
            if dfs(preq, course):
                res.append(True)
            else:
                res.append(False)

        return res


numCourses = 3
prerequisites = [[1, 2], [1, 0], [2, 0]]
queries = [[1, 0], [1, 2]]
output = [True, True]

obj = Solution()
res = obj.checkIfPrerequisite(numCourses, prerequisites, queries)
print(res)
print(output)
print(res == output)
