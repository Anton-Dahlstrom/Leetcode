class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        res = []

        def nestedLoop(i, arr):
            if len(arr) == k:
                res.append(arr.copy())
                return
            for j in range(i+1, n+1):
                arr.append(j)
                nestedLoop(j, arr)
                arr.pop()
        nestedLoop(0, [])
        return res


n = 4
k = 2
output = [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]

obj = Solution()
res = obj.combine(n, k)
print(res)
print(output)
print(res == output)
