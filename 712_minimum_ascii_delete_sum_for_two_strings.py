class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n, m = len(s1), len(s2)
        if n > m:
            return self.minimumDeleteSum(s2, s1)
        res = 0
        for c in s1:
            res += ord(c)
        for c in s2:
            res += ord(c)

        # maximize value from non-deleted chars
        dp = [0] * m
        for i in range(n):
            temp = [0] * m
            for j in range(m):
                prev = 0
                cur = 0
                if s1[i] == s2[j]:
                    cur = ord(s1[i])*2
                if j:
                    prev = dp[j-1]
                temp[j] = max(dp[j], cur+prev, temp[j-1])
            dp = temp
        return res - dp[-1]


s1 = "delete"
s2 = "leet"
output = 403

obj = Solution()
res = obj.minimumDeleteSum(s1, s2)
print(res)
print(output)
print(res == output)
