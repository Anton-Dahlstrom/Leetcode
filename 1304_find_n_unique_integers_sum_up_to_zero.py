class Solution:
    def sumZero(self, n: int) -> list[int]:
        res = []
        cur = 1
        for i in range(0, n-1, 2):
            res.append(cur)
            res.append(-cur)
            cur += 1
        if len(res) < n:
            res.append(0)
        return res


n = 1
output = [0]

obj = Solution()
res = obj.sumZero(n)
print(res)
print(output)
print(res == output)
