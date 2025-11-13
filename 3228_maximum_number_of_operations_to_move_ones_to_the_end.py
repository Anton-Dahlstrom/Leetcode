class Solution:
    def maxOperations(self, s: str) -> int:
        s += "1"
        n = len(s)
        res = 0
        ones = 0
        if s[0] == "1":
            ones += 1

        for i in range(1, n):
            if s[i] == "1":
                if s[i-1] == "0":
                    res += ones
                ones += 1
        return res


s = "1001101"
output = 4

obj = Solution()
res = obj.maxOperations(s)
print(res)
print(output)
print(res == output)
