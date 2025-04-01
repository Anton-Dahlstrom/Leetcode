
class Solution:
    def longestCycle(self, edges: list[int]) -> int:
        n = len(edges)
        rank = [0]*n
        for edge in edges:
            if edge >= 0:
                rank[edge] += 1
        arr = [i for i in range(n) if not rank[i]]
        # use khans algo to eliminate all nodes not part of a cycle
        while arr:
            cur = arr.pop()
            node = edges[cur]
            if node == -1:
                continue
            rank[node] -= 1
            if not rank[node]:
                arr.append(node)

        res = -1
        for i in range(n):
            if not rank[i]:
                continue
            j = edges[i]
            cnt = 0
            while j >= 0 and rank[j]:
                rank[j] -= 1
                cnt += 1
                if j == i:
                    res = max(res, cnt)
                    break
                j = edges[j]

        return res


edges = [2, -1, 3, 1]
output = -1

obj = Solution()
res = obj.longestCycle(edges)
print(res)
print(output)
print(res == output)
