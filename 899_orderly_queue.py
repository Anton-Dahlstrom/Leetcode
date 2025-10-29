class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k >= 2:
            return "".join(sorted(list(s)))
        n = len(s)
        start = float("inf")
        for i in range(n):
            cur = ord(s[i])
            if cur < start:
                start = cur
        start = chr(start)
        res = s
        for i in range(n):
            if s[i] != start:
                continue
            cur = s[i:] + s[:i]
            if cur < res:
                res = cur
        return res


s = "baaca"
k = 3
output = "aaabc"


obj = Solution()
res = obj.orderlyQueue(s, k)
print(res)
print(output)
print(res == output)
