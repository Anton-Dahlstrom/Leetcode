class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        nodes = {}
        for left, right in edges:
            if right in nodes:
                nodes[right].append(left)
            else:
                nodes.setdefault(left, []).append(right)

        visited = set()
        roots = set()

        def dfs(val):
            if val in nodes:
                for child in nodes[val]:
                    if child in visited:
                        return False
                    if child in roots:
                        roots.remove(child)
                    visited.add(child)
                    if not dfs(child):
                        return False
            return True

        for num in nodes:
            if num not in visited:
                roots.add(num)
                if not dfs(num):
                    return False

        if len(roots) > 1:
            return False
        return True


n = 5
edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
output = False


obj = Solution()
res = obj.validTree(n, edges)
print(res)
print(res == output)
