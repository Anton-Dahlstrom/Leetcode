class Solution:
    def divideString(self, s: str, k: int, fill: str) -> list[str]:
        res = []
        n = len(s)
        for i in range(0, n, k):
            res.append(s[i:i+k])
        res[-1] += fill * (k-len(res[-1]))
        return res


s = "abcdefghi"
k = 3
fill = "x"
output = ["abc", "def", "ghi"]

obj = Solution()
res = obj.divideString(s, k, fill)
print(res)
print(output)
print(res == output)
