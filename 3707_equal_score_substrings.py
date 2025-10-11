class Solution:
    def scoreBalance(self, s: str) -> bool:
        n = len(s)
        total = 0
        for i in range(n):
            total += ord(s[i]) - 96
        cur = 0
        for i in range(n):
            val = ord(s[i]) - 96
            cur += val
            total -= val
            if cur == total:
                return True
            elif cur > total:
                return False
        return False


s = "adcb"
output = True


obj = Solution()
res = obj.scoreBalance(s)
print(res)
print(output)
print(res == output)
