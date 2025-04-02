class Solution:
    def possibleBipartition(self, n: int, dislikes: list[list[int]]) -> bool:
        g1 = set()
        g2 = set()
        edges = [[] for _ in range(n+2)]
        for edge in dislikes:
            v1, v2 = edge
            edges[v1].append(v2)
            edges[v2].append(v1)

        visit = set()

        def dfs(left, node):
            if node in visit:
                return True
            visit.add(node)
            for edge in edges[node]:
                if left:
                    if edge in g1:
                        return False
                    g2.add(edge)
                else:
                    if edge in g2:
                        return False
                    g1.add(edge)
                if not dfs(left == False, edge):
                    return False
            return True

        for i in range(1, n+1):
            if i not in visit:
                g1.add(i)
            if not dfs(True, i):
                return False
        return True


n = 5
dislikes = [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]]
output = False


obj = Solution()
res = obj.possibleBipartition(n, dislikes)
print(res)
print(output)
print(res == output)
