class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        edges = {}
        for course, prerequisit in prerequisites:
            edges.setdefault(course, []).append(prerequisit)

        def dfs(val):
            for edge in edges[val]:
                if edge in visited:
                    return True
                if edge in edges:
                    visited.add(edge)
                    if dfs(edge):
                        return True
                    visited.remove(edge)
            if val not in safe:
                safe.add(val)
                res.append(val)
        res = [i for i in range(numCourses) if i not in edges]
        safe = set()
        for node in edges:
            if node in edges and node not in safe:
                visited = set()
                visited.add(node)
                if dfs(node):
                    return []
        return res


numCourses = 4
prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
output = [0, 2, 1, 3]

obj = Solution()
res = obj.findOrder(numCourses, prerequisites)
print(res)
print(res == output)
