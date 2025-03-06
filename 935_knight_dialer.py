class Solution:
    def knightDialer(self, n: int) -> int:
        edges = {1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [3, 9, 0], 5: [], 6: [
            1, 7, 0], 7: [2, 6], 8: [1, 3], 9: [4, 2], 0: [4, 6]}

        visited = {}

        def dfs(cur, depth):
            if not depth:
                return 1
            if (cur, depth) in visited:
                return visited[(cur, depth)]
            res = 0
            for num in edges[cur]:
                res += dfs(num, depth-1)

            visited[(cur, depth)] = res
            return res

        res = 0
        for i in range(0, 10):
            res += dfs(i, n-1)
        return res % (10**9 + 7)


n = 2
output = 20

obj = Solution()
res = obj.knightDialer(n)
print(res)
print(output)
print(res == output)
