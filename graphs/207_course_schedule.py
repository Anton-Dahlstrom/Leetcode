class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:

        needs = {}
        for cour, need in prerequisites:
            needs.setdefault(cour, []).append(need)

        def dfs(val):
            if val == self.search:
                return True
            if not self.search:
                self.search = val
                print(self.search)
            else:
                visited.add(val)
            for v in needs[val]:
                if v in needs and v not in visited and v not in safe:
                    if dfs(v):
                        return True
            return False

        self.search = None
        safe = set()
        # Checks if each number loops back to itself.
        for n1, n2 in prerequisites:
            self.search = None
            visited = set()
            if dfs(n1):
                return False
            safe.add(n1)

        return True


numCourses = 3
prerequisites = [[1, 0], [1, 2], [0, 1]]
output = False

numCourses = 5
prerequisites = [[1, 4], [2, 4], [3, 1], [3, 2]]
output = True


obj = Solution()
res = obj.canFinish(numCourses, prerequisites)
print(res)
print(res == output)
